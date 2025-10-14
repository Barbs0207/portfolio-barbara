import google.generativeai as genai

# Sua chave de API
genai.configure(api_key="AIzaSyDiYuxLzJtx9jzj-qOpnNDBL-z-IOr4kZA")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)