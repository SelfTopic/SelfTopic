<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-ghoul.svg">
  <img alt="CheStor — Self: бэкенд на Python, Telegram Bot API, «Токийский гуль»" src="assets/banner-human.svg" width="100%">
</picture>

Пишу бэкенд на Python и неровно дышу к Telegram Bot API: написал к нему свой фреймворк, а по
«Токийскому гулю» — RPG-бота. Всё это собрано на **[chestor.site](https://chestor.site)** — сайте
в виде Telegram-клиента, где чат синхронизирован с настоящей Telegram-группой.

*Backend developer (Python). Author of [selfrotgram](https://github.com/SelfTopic/selfrotgram), a
typed Telegram Bot API framework, and [chestor_bot](https://github.com/SelfTopic/chestor_bot), a Tokyo
Ghoul RPG game in Telegram.*

> [!TIP]
> **Хочешь поиграть в «Токийского гуля» в Telegram?** Напиши [@chestor_chat_bot](https://t.me/chestor_chat_bot)
> `/start` — или добавь его в чат. Гуль с голодом и кагуне, дуэли, бои с мобами, своя экономика.
> Все команды — в канале [@CheStorCommands](https://t.me/CheStorCommands).

## Проекты

Ранги — шкала угрозы CCG, как на [сайте](https://chestor.site/c/projects).

| Ранг | Проект | Что это |
| :-: | :-- | :-- |
| **SSS** | [chestor_bot](https://github.com/SelfTopic/chestor_bot) | RPG-бот по «Токийскому гулю»: голод, смерть и возрождение, кагуне четырёх типов, дуэли и бои с мобами, экономика. v1.0.0, 659 тестов. [Досье →](https://chestor.site/bot) |
| **SS** | [selfrotgram](https://github.com/SelfTopic/selfrotgram) | Асинхронный фреймворк для Telegram Bot API, где типы говорят правду: фильтр гарантирует поле — тип это знает. Кодогенерация из спецификации Bot API 10.3, CLI. [PyPI](https://pypi.org/project/selfrotgram/) · [подробнее →](https://chestor.site/selfrotgram) |
| **S** | [questions_ghoul_api](https://github.com/SelfTopic/questions_ghoul_api) | База вопросов викторины по «Токийскому гулю»: Express 5, PostgreSQL, Redis, одноразовые refresh-токены. Работает на `chestor.site/api`, клиент на Python — [ghoul-quiz-lib](https://github.com/SelfTopic/questions_ghoul_api_lib). |
| **S** | [chestor_site](https://github.com/SelfTopic/chestor_site) | Этот самый сайт: Next.js + сервис чата на selfrotgram, капча на Ghoul Quiz, модерация из группы. |
| **A** | [userbot-api](https://github.com/SelfTopic/userbot-api) | HTTP API над тестовыми Telegram-аккаунтами, чтобы Claude Code проверял ботов в настоящем Telegram. |
| **A** | [voice-player](https://github.com/SelfTopic/voice-player) | «Джарвис» для KDE Plasma: быстрые команды офлайн через Vosk, свободные запросы через faster-whisper. |
| **B** | [tiktok-userbot](https://github.com/SelfTopic/tiktok-userbot) | Кинул ссылку на TikTok в чат — получил видео или слайдшоу. |

## Стек

**Python** — asyncio, aiohttp, pydantic, SQLAlchemy 2, Alembic, pytest, pyright, Poetry<br>
**Telegram** — selfrotgram, aiogram 3, grammY, Pyrogram / Kurigram<br>
**TypeScript** — Node.js, Express 5, Next.js, Drizzle, Zod, Vitest<br>
**Данные и инфраструктура** — PostgreSQL, Redis, Docker Compose, nginx, GitHub Actions

## Связь

[Telegram @chestor](https://t.me/chestor) · [chestor.official@gmail.com](mailto:chestor.official@gmail.com) · [chestor.site](https://chestor.site)

> *In code I trust, for it never lies or betrays — it simply executes.*
