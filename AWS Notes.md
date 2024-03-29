# AWS EC2
## EC2 Instance Types
To upgrade instance type, go to EC2 control panel:
1. Stop the instance
2. Instance State -> Change Instance Type
3. Start instance and pray

## Cloning into EC2 Instance
`git clone https://username@<githublink>.git -b <branch>`

Note: Password needs to be a temporary Personal Access Token:
- Github settings > Developer settings > Personal access tokens > Generate new token

## Connections
### Security
Remember to poke a hole for your IP / port to connect to the Instance.
- SSH Port: 22
- MySQL Port: 3306
- Standard backend port: 80 | 8000 | 8080

### SSH
`ssh -i "key.pem" username@public_dns`
- Click Connect > SSH client on dashboard to get a customized one for the instance.
- key.pem is the private key file created on instance creation
- username is the default username
- public_dns is the public IP

### Testing with curl
- GET: `curl http://public_dns:port/route`
- POST: `curl -X POST -H "Content-Type: application/json" http://public_dns:port/route -d @request.json`

## Hosting
### Running processes in background - use for first Docker build and API hosting
1. `screen` creates a screen terminal
   - `screen -S session_name` starts a named screen if multiple screens are needed
2. Run processes within the screen
3. Detach using `Ctr-a-d` to let it run in background
4. Resume screen with `screen -r session_name`
5. Quit screen with `Ctr-a-k` within screen or `screen -X -S session_name quit` from outside screen

### Docker
- Build image (current directory = .): `docker build -t image_name directory`
- Start container: `docker run -d --name container_name -p host_port:container_port image_name`
- List containers: `docker ps -q`
- Kill container: `docker kill container_name`
- Remove container after force-stopping: `docker rm -f container_name`
- Remove all stopped containers: `docker system prune`

## Terminal syntax
- See files in directory: `dir`
- Delete folder with subfolders: `rm -rf folder_name`