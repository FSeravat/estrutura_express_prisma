import subprocess
import os
import json

def create_express():
    #Criando o arquivo package.json
    subprocess.run("yarn init", shell=True)

    #Instalando dependências
    subprocess.run("yarn add express && yarn add -D @types/express", shell=True)
    subprocess.run("yarn add -D typescript", shell=True)
    subprocess.run("yarn add -D ts-node-dev", shell=True)

    #Permitindo compilar typescript
    subprocess.run("yarn tsc --init", shell=True)

    #criando estrutura de pasta
    if not os.path.exists("src"):
        os.mkdir("src")
    server_file = open(os.path.join("src","server.ts"),mode="w")
    server_file.write(
"""import express from 'express'
import { Router, Request, Response } from 'express';

const app = express();

const route = Router()

app.use(express.json())

route.get('/', (req: Request, res: Response) => {
  res.json({ message: 'hello world with Typescript' })
})

app.use(route)


app.listen(3333, () => 'server running on port 3333')"""
    )
    server_file.close()

    #Alterando o arquivo package.json
    package_json = json.load(open("package.json"))
    package_json["scripts"] = dict()
    package_json["scripts"]["dev"] = "ts-node-dev --inspect --transpile-only --ignore-watch node_modules src/server.ts"
    json.dump(package_json,open("package.json",mode="w"),indent=4)

def create_prisma():
    #instalando dependencias
    subprocess.run("yarn add -D prisma", shell=True)
    subprocess.run("yarn add -D @prisma/client", shell=True)

    #Iniciando o prisma
    subprocess.run("yarn prisma init --datasource-provider sqlite", shell=True)

try:
    create_express()
    create_prisma()
except Exception as error:
    print(error)
    os.system("pause")