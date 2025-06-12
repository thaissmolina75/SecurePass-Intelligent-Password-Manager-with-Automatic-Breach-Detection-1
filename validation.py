
import hashlib
import requests # Para hacer peticiones HTTP a la API de Have I Been Pwned



class passwordChecker:
    @staticmethod
    def verification (password):
        #encode password
        encodedPasword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix  = encodedPasword[:5]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)
        if response.status_code == 200:
            hashes = response.text.splitlines()
            suffix = encodedPasword[5:]
            if any(suffix == h.split(':')[0] for h in hashes):
                print("⚠️ Tu contraseña ha sido comprometida. Es recomendable cambiarla.")
                return True
            else:
                print("✅ Tu contraseña parece segura.")
                return False
        else:
            print("❌ Error al obtener datos de la API.")
            return None

             

