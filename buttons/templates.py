from string import Template

say_lang = {
    "ru": """Установлен 🇷🇺 Русский язык""",
    "en": """Language changed to 🇬🇧 English""",
    "cn": """语言已更改为 🇨🇳 中文"""
    }

say_help = {
    "ru": """Если что-то пошло не так, просто введите: /start или перезапустите бота, чтобы сбросить его.

или свяжитесь с 👉 @iatikhonov 👈 для получения дополнительной помощи!""",
    "en": """If anything went wrong, just type: /start or restart the Bot to reset it.

or contact 👉 @iatikhonov 👈 for more help!""",
    "cn": """如遇功能异常，请输入： /start 或重启 Bot 进行重置

或 联系👉 @iatikhonov 👈获取更多帮助!"""
}

role = {
    "ru": Template("""
Моя роль как помощника по искусственному интеллекту теперь следующая:

**$system_content**

Теперь вы можете отправить мою новую роль напрямую!

Если вы хотите отменить эту настройку, просто ответьте: `отмена`‍ 
"""),
    "en": Template("""
As an AI assistant, my role is now set as🤖：:

**$system_content**

Now you can send my new role directly!


In case you want to stop this setting, just reply: `cancel`‍
"""),
    "cn": Template("""
您当前的系统AI助手身份设置为🤖：

**$system_content**

请直接回复新的AI助手身份设置！

您可以参考： [🧠ChatGPT 中文调教指南]https://github.com/PlexPt/awesome-chatgpt-prompts-zh

如需取消重置，请直接回复：`取消` 或 `取消重置` ‍
""")}

context_info = {
    "ru": Template("""
Каждый раз когда вы задаете вопрос ИИ дает ответ, учитывая ваши последние $context_count сообщений!

История очищена!
"""),
    "en": Template("""
Each time you ask a question, the AI will provide an answer considering your most recent $context_count conversations!

Your conversation history has now been cleared, and you can start asking questions again!
"""), 
    "cn": Template("""
每次提问AI会参考您最近 $context_count 次的对话记录为您提供答案！

现在您的会话历史已清空，可以重新开始提问了！
""")}

identity_confirmed = {
    "ru": """
Новая личность для ИИ-помощника подтверждена.
Я отвечу на ваши вопросы, основываясь на этой новой личности.
Вы можете начать задавать вопросы прямо сейчас!
""",
    "en": """
The new AI assistant identity has been confirmed.
I will answer your questions based on this new identity.
You can start asking questions now!
""",
    "cn": """
新的AI助手身份已确认。
我将以新身份为背景来为您解答问题。
您现在可以开始提问了！
"""}

statistics_response = {
    "ru": Template("""
Привет, $user!

Ваше текущее использование токенов:

Запросы: $prompt_tokens
Ответы: $completion_tokens 
Итого: $total_tokens

Хорошего дня! 🎉
"""),
    "en": Template("""
Hi $user!

Your current Token usage is as follows:

Query: $prompt_tokens Tokens
Answer: $completion_tokens Tokens
Total: $total_tokens Tokens

Have a nice day!🎉
"""), 
    "cn": Template("""
Hi  $user!

您当前Token使用情况如下：

查询：$prompt_tokens Tokens
答案：$completion_tokens Tokens
总共：$total_tokens Tokens

祝您生活愉快！🎉
""")}

token_limit = {
    "ru": Template("""
$answer

Длина ответа превысила текущий максимальный лимит токенов $max_token на ответ.
Пожалуйста, свяжитесь с @iatikhonov если хотите снять ограничения! ✅
"""),
    "en": Template("""
$answer

The length of the response exceeded the current maximum token limit $max_token per response.
Please contact @iatikhonov if you want to remove restrictions! ✅
"""),
    "cn": Template("""
$answer

响应的长度超出了当前每个响应的最大令牌限制 $max_token。
如果您想取消限制，请联系 @iatikhonov！✅
""")}

start_responce = {
    "ru": ("""
Привет! Я чат-бот с искусственным интеллектом, созданный для взаимодействия с вами с целью улучшения вашей жизни и чтобы сделать ваш день немного ярче. Если у вас есть вопросы или вы просто хотите дружески поболтать, я здесь чтобы помочь! 🤗

Я могу помочь вам с любым вопросом, от совета до анекдота, и я доступен 24 часа в сутки 7 дней в неделю! 🕰️

Я могу быть вашим генеральным помощником или помощником по программированию, основная цель которого помочь вам в меру собсвенных возможностей анализа большого количества данных, или психологом, мотиватором или даже Илоном Маском 🤟

Просто используйте меню «Switch Roles», чтобы изменить мою роль, или настройте свою собственную роль с помощью опции «Customize Role» 🙏️️️️️️️

Так почему бы не поделиться мной со своими друзьями? 😍

Вы можете отправить им эту ссылку: https://t.me/VassermannBot 🎂️️️️️️️

Также вы можете обратиться к администратору @iatikhonov для снятия ограничения на объём сообщений 💵️️️️️️
"""),
    "en": ("""
Hi! I'm an AI chatbot created to interact with you and make your day a little brighter. If you have any questions or just want to have a friendly chat, I'm here to help! 🤗

Do you know what's great about me? I can help you with anything from giving advice to telling you a joke, and I'm available 24/7! 🕰️

I can be your General or Code Assistant, that primary goal is to assist you to the best of your ability, or Psychologist, Motivator, or even Elon Musk 🤟 

Just use Switch Roles menu to change my, or customize your own role by Customize Role option 🙏️️️️️️

So why not share me with your friends? 😍

You can send them this link: https://t.me/VassermannBot 🎂️️️️️️

You can also contact administrator @iatikhonov to remove message volume restrictions 💵️️️️️️
"""),
    "cn": ("""
你好！ 我是一个人工智能聊天机器人，旨在与您互动，改善您的生活，让您的一天更加美好。 如果您有疑问或只是想进行友好聊天，我随时为您提供帮助! 🤗

我可以为您提供从建议到轶事的任何帮助，并且每周 7 天、每天 24 小时为您服务! 🕰️

我可以成为你的总助理或代码助理，主要目标是尽你所能帮助你，也可以成为心理学家、激励者甚至埃隆·马斯克 🤟

只需使用“切换角色”菜单来更改我的角色，或使用“自定义角色”选项自定义您自己的角色 🙏️️️️️️️

那么为什么不与你的朋友分享我呢? 😍

您可以向他们发送此链接：https://t.me/VassermannBot 🎂️️️️️️️

您也可以联系管理员 @iatikhonov 取消消息量限制 💵️️️️️️
""")}