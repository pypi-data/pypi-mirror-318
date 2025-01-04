# `vault-secret-manager`

A HashiCorp Vault AppRole Secrets Manager

You must set VAULT_ADDR and VAULT_TOKEN or define them in a .env file.

Example:

VAULT_ADDR=&quot;https://vault.example.com:8200&quot;

VAULT_TOKEN=&quot;XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&quot;

**Usage**:

```console
$ vault-secret-manager [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `list`: List AppRole Secrets for Role in Namespace
* `get`: Get specific AppRole Secret details

## `vault-secret-manager list`

List AppRole Secrets for Role in Namespace

**Usage**:

```console
$ vault-secret-manager list [OPTIONS] ROLE NAMESPACE
```

**Arguments**:

* `ROLE`: [required]
* `NAMESPACE`: [required]

**Options**:

* `--help`: Show this message and exit.

## `vault-secret-manager get`

Get specific AppRole Secret details

**Usage**:

```console
$ vault-secret-manager get [OPTIONS] SECRET_ID_ACCESSOR NAMESPACE
```

**Arguments**:

* `SECRET_ID_ACCESSOR`: [required]
* `NAMESPACE`: [required]

**Options**:

* `--help`: Show this message and exit.
