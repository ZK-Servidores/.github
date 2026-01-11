import requests
import re

STEAM_API_KEY = "STEAM_APIKEY" # Ou use segredos do GitHub
STEAM_ID_64 = "76561198088290585"
README_PATH = "/profile/README.md"

# URL da API para obter o sumário do perfil
url = f"api.steampowered.com{STEAM_API_KEY}&steamids={STEAM_ID_64}"

response = requests.get(url)
data = response.json()
avatar_url = data['response']['players'][0]['avatarfull'] # URL da imagem grande

# Atualiza o README
with open(README_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Usa regex para encontrar e substituir a linha que contém a imagem do avatar
# Certifique-se de ter um marcador no seu README, por exemplo: <!-- STEAM_AVATAR_START --> <!-- STEAM_AVATAR_END -->
new_avatar_markdown = f"![Avatar Steam]({avatar_url})"
updated_content = re.sub(r"<!-- STEAM_AVATAR_START -->.*?<!-- STEAM_AVATAR_END -->", f"<!-- STEAM_AVATAR_START -->{new_avatar_markdown}<!-- STEAM_AVATAR_END -->", content, flags=re.DOTALL)

with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(updated_content)
