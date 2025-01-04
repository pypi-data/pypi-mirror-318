from dotenv import load_dotenv
import datetime
import hvac
import logging
import os
import pytz
import sys
import typer
import warnings

load_dotenv()
app = typer.Typer()

VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

if VAULT_ADDR is None or VAULT_TOKEN is None:
    print("You must set VAULT_ADDR and VAULT_TOKEN or define them in a .env file.")
    sys.exit(1)


warnings.filterwarnings("ignore", category=DeprecationWarning)

logname = "vault-secret-checker.log"

logging.basicConfig(
    filename=logname,
    filemode="a",
    format="%(asctime)s.%(msecs)d %(name)s %(levelname)s -- %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger("vault-secret-checker")
logger.info("Starting Vault Secret Checker")


def time_parser(time_string):
    """Parses the time string into a datetime object"""
    try:
        parts = time_string.split(".")
        dt = parts[0]
        offset = parts[1].split("-")
        time_string = dt + "_" + "-" + offset[1]
        format_data = "%Y-%m-%dT%H:%M:%S_%z"
        time_obj = datetime.datetime.strptime(time_string, format_data)
        return time_obj
    except (ValueError, IndexError) as e:
        logger.error("Error parsing time string: %s", time_string)
        logger.error("Assigning epoch date")
        logger.error("Error: %s", e)
        time_obj = datetime.datetime.fromtimestamp(0, pytz.utc)
        return time_obj


class VaultSecretID:
    """Vault Secret ID Object Class"""

    def __init__(
        self,
        accessor_id,
        role_name,
        namespace,
        creation,
        expiration,
        number_of_uses,
        address,
        token,
    ):
        self.accessor_id = accessor_id
        self.role_name = role_name
        self.namespace = namespace
        self.creation = time_parser(creation)
        self.expiration = time_parser(expiration)
        self.number_of_uses = int(number_of_uses)
        self.address = address
        self.token = token

    def __str__(self):
        return f"ID: {self.accessor_id}, Role: {self.role_name}, Namespace: {self.namespace}, Creation: {self.creation}, Expiration: {self.expiration}, Remaining Uses: {self.number_of_uses}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (
            self.accessor_id == other.accessor_id and self.namespace == other.namespace
        )

    def lookup(self):
        """Looks up the Secret ID in the Vault"""
        client = hvac.Client(
            url=self.address, token=self.token, namespace=self.namespace
        )
        path = "auth/approle/role/" + self.role_name + "/secret-id-accessor/lookup"
        properties = client.write(path, secret_id_accessor=self.accessor_id)
        properties = properties["data"]
        return properties

    def destroy(self):
        """Destroys the Secret ID in the Vault"""
        client = hvac.Client(
            url=self.address, token=self.token, namespace=self.namespace
        )
        path = "auth/approle/role/" + self.role_name + "/secret-id-accessor/destroy"
        client.write(path, secret_id_accessor=self.accessor_id)


@app.callback()
def callback():
    """
    A HashiCorp Vault AppRole Secrets Manager

    You must set VAULT_ADDR and VAULT_TOKEN or define them in a .env file.

    Example:

    VAULT_ADDR="https://vault.example.com:8200"

    VAULT_TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    """


@app.command()
def list(role: str, namespace: str):
    """
    List AppRole Secrets for Role in Namespace
    """
    client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN, namespace=namespace)
    path = f"auth/approle/role/{role}/secret-id"
    ids = client.list(path)
    if ids:
        if "data" in ids:
            logger.info(f"Secret IDs for Role: {role} in Namespace: {namespace}")
            for id in ids["data"]["keys"]:
                accessor_id = id
                lookup_path = path = (
                    f"auth/approle/role/{role}/secret-id-accessor/lookup"
                )
                properties = client.write(lookup_path, secret_id_accessor=id)
                namespace = namespace
                properties = properties["data"]
                creation = properties["creation_time"]
                expiration = properties["expiration_time"]
                number_of_uses = properties["secret_id_num_uses"]
                number_of_uses = int(number_of_uses)
                secret_id = str(id)
                secret_id = VaultSecretID(
                    accessor_id,
                    role,
                    namespace,
                    creation,
                    expiration,
                    number_of_uses,
                    VAULT_ADDR,
                    VAULT_TOKEN,
                )
                logger.info(secret_id)
                typer.echo(secret_id)


@app.command()
def get(secret_id_accessor: str, namespace: str):
    """
    Get specific AppRole Secret details
    """
    client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN, namespace=namespace)
    roles = (client.list("auth/approle/role"))["data"]["keys"]
    for role in roles:
        path = "auth/approle/role/" + role + "/secret-id"
        ids = client.list(path)
        if ids:
            if "data" in ids:
                logger.info(f"Secret IDs for Role: {role} in Namespace: {namespace}")
                for id in ids["data"]["keys"]:
                    accessor_id = id
                    if id == secret_id_accessor:
                        print(f"Found Secret ID: {id} for Role: {role}")
                        found_id = id
                        lookup_path = path = (
                            "auth/approle/role/" + role + "/secret-id-accessor/lookup"
                        )
                        properties = client.write(lookup_path, secret_id_accessor=id)
                        namespace = namespace
                        properties = properties["data"]
                        creation = properties["creation_time"]
                        expiration = properties["expiration_time"]
                        number_of_uses = properties["secret_id_num_uses"]
                        number_of_uses = int(number_of_uses)
                        secret_id = str(id)
                        secret_id = VaultSecretID(
                            accessor_id,
                            role,
                            namespace,
                            creation,
                            expiration,
                            number_of_uses,
                            VAULT_ADDR,
                            VAULT_TOKEN,
                        )
                        logger.info(secret_id)
                        typer.echo(secret_id)
                        return secret_id
        else:
            logger.info(f"No Secret IDs for Role: {role} in Namespace: {namespace}")
            typer.echo(f"No Secret IDs for Role: {role} in Namespace: {namespace}")
    message = f"Secret ID {secret_id_accessor} not found in Vault"
    logger.info(message)
    typer.echo(message)
    sys.exit(1)
