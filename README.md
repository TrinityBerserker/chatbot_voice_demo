# 🤖 Chatbot de Voz y Texto con Python + OpenAI

---

## 📌 Descripción

### 🇪🇸 Español
Este proyecto es una demo de un chatbot conversacional en español, construido con Python. Permite al usuario interactuar con el asistente mediante entrada de voz (si tiene micrófono) o escribiendo texto. El asistente genera respuestas usando la API de OpenAI (GPT) y las reproduce con síntesis de voz. Es una base ideal para desarrollar asistentes virtuales más avanzados con funcionalidades conversacionales naturales.

### 🇬🇧 English
This project is a demo of a Spanish-language conversational chatbot built with Python. It allows users to interact with the assistant via voice input (if a microphone is available) or by typing. The assistant uses the OpenAI API (GPT) to generate responses and reads them aloud using speech synthesis. It's a great foundation for developing more advanced virtual assistants with natural conversation capabilities.

### 🇷🇺 Русский
Этот проект — демонстрация голосового чат-бота на испанском языке, созданного с помощью Python. Пользователь может взаимодействовать с ботом голосом (при наличии микрофона) или через текстовый ввод. Ответы генерируются с помощью API OpenAI (GPT) и озвучиваются с помощью синтеза речи. Отличная основа для разработки более сложных виртуальных помощников с естественным общением.



```markdown
# 🤖 Chatbot de Voz y Texto con Python + OpenAI

Este es un demo de asistente conversacional en español que permite interactuar mediante voz (si tienes micrófono) o entrada de texto manual. Utiliza la API de OpenAI para responder inteligentemente y sintetiza la respuesta con voz.

---

## 🌍 Idiomas disponibles:
- 🇪🇸 Español
- 🇬🇧 English
- 🇷🇺 Русский

---

## 🇪🇸 Español

### 🧠 Tecnologías utilizadas
- `openai` (GPT-3.5-turbo)
- `SpeechRecognition` + `Whisper API`
- `pyttsx3` (texto a voz)
- `dotenv` (gestión de variables de entorno)

### 🚀 Cómo ejecutar
1. Clona el repositorio.
2. Crea un archivo `.env` y coloca tu clave API:
```

OPENAI\_API\_KEY=tu\_clave\_aquí

````
3. Instala dependencias:
```bash
pip install openai python-dotenv pyttsx3 SpeechRecognition
````

> Si da error con PyAudio, consulta cómo instalarlo desde rueda (.whl).

4. Ejecuta:

   ```bash
   python main.py
   ```

### 📌 Características

* Entrada por texto o por voz
* Conversación fluida con ChatGPT
* Síntesis de voz en español

---

## 🇬🇧 English

### 🧠 Technologies used

* `openai` (GPT-3.5-turbo)
* `SpeechRecognition` + `Whisper API`
* `pyttsx3` (text-to-speech)
* `dotenv` (environment variable management)

### 🚀 How to run

1. Clone the repository.
2. Create a `.env` file and add your API key:

   ```
   OPENAI_API_KEY=your_key_here
   ```
3. Install dependencies:

   ```bash
   pip install openai python-dotenv pyttsx3 SpeechRecognition
   ```

   > If `PyAudio` fails, use `.whl` installation.
4. Run:

   ```bash
   python main.py
   ```

### 📌 Features

* Text or voice input
* Natural conversation with ChatGPT
* Spanish voice output

---

## 🇷🇺 Русский

### 🧠 Используемые технологии

* `openai` (GPT-3.5-turbo)
* `SpeechRecognition` + `Whisper API`
* `pyttsx3` (преобразование текста в речь)
* `dotenv` (переменные среды)

### 🚀 Как запустить

1. Клонируйте репозиторий.
2. Создайте файл `.env` и добавьте ваш API-ключ:

   ```
   OPENAI_API_KEY=ваш_ключ_здесь
   ```
3. Установите зависимости:

   ```bash
   pip install openai python-dotenv pyttsx3 SpeechRecognition
   ```

   > Если возникнут проблемы с PyAudio, установите через `.whl`.
4. Запуск:

   ```bash
   python main.py
   ```

### 📌 Возможности

* Ввод с клавиатуры или голосом
* Разговор на естественном языке с ChatGPT
* Озвучивание ответа на испанском языке

---

## 🛠️ Notas adicionales

* Puedes cambiar el idioma del asistente ajustando el `prompt` del sistema en el código.
* Se requiere una clave de API válida de OpenAI.
* El sistema es ideal como punto de partida para asistentes inteligentes o chatbots por voz.

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la **GNU General Public License v3.0**.

Puedes:

- Usar, estudiar y modificar el código.
- Distribuir copias del software (modificadas o no), siempre que mantengas la misma licencia.
- Usar este código en proyectos personales o comerciales, respetando los términos.

**Este software se entrega SIN NINGUNA GARANTÍA**, incluso sin la garantía implícita de COMERCIABILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR.

Para más detalles, consulta el texto completo de la licencia en:  
📄 https://www.gnu.org/licenses/gpl-3.0.html


```
