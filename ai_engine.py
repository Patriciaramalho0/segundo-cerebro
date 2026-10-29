import os
from openai import OpenAI

class AIBrain:
    def __init__(self):
        # Pega a chave de forma segura do ambiente ou deixa pronto para o usuário inserir
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

    def ask(self, prompt, system_prompt="Você é um assistente útil."):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro na IA: Verifique se a Chave da OpenAI está configurada. (Detalhe: {e})"