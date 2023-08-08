The run to see the server running, you can also get your token from here

```
vault server -dev
```

1. READ - For reading the secrets from the vault
2. WRITE/PUT - For writing the secrets inside the vault
## See list of paths available
$ vault secrets list

## WRITE SECRET ##
$ vault kv put secret/path my-key-1=vaule-1

## READ SECRET ##
$ vault kv get secret/path

## DELETE SECRET ##
$ vault kv delete secret/path

