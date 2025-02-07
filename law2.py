from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()


print("Starting the bot...")

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '8027903301:AAHKOCKvqUPMyzs0pMbIVM2IZ4Yye-MpjRY'
BOT_USERNAME: Final = '@law1_students_bot'

user_states = {}

# Command Handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text( 
    'أهلاً وسهلاً بك في بوت Law Students! \U00002696\U0001F4AC أنا هنا عشان أساعدك وبرمجوني أرد على إحدى الكلمات التالية:\n'
    '\n (انضمام - استفسار - سؤال - شكوى - مشكلة - اقتراح) \n'
    "\n"
    'ما عليك أوعدك بعدين أطور نفسي وأكون بوت قانوني متطور\U0001F916\U00002B06🏻! \n' 'وأصير أقدر أحول الرسائل للمشرفين وأخليك تدردش معهم\U0001F607 \n'
    'ولا أقولك أنا بصير أدردش معك وأحسن من الذكاء الاصطناعي\U0001F60F \n'
    'بس لازم أطور نفسي أول ✅. \n\n المهم كيف أقدر أخدمك ؟\n\n'
)

def handle_response(text: str, state: dict) -> str:
    processed: str = text.lower()

    if 'انضمام' in processed:
        state['awaiting_level'] = True
        return (
            'نحن سعداء بأنك تريد الانضمام إلى مجموعات المستويات الدراسية لكلية الحقوق ⚖️✅، '
            'من فضلك حدّد/ي لنا المستوى المطلوب من خلال إرسال إحدى الكلمات الآتية: \n'
            '(اول - ثاني - ثالث - رابع - خامس - سادس - سابع - ثامن)'
        )

    if state.get('awaiting_level'):
        state['awaiting_level'] = False
        if 'اول' in processed or 'أول' in processed or 'مستوى اول' in processed or 'المستوى الاول' in processed or 'مستوى أول' in processed or 'مستوى اول' in processed:
            return (
                'مسيرتك الجامعية أبتدت الآن! 📝\n'
                'عشان نضيفك للمجموعة، أرسل/ي لمشرف المجموعة، عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'لو عندك أي استفسار أو محتاج مساعدة، المشرف دايمًا موجود ومستعد يساعدك!'
            )
        if 'ثاني' in processed or 'مستوى ثاني' in processed or 'المستوى الثاني' in processed:
            return (
                'مرحباً فيك في المستوى الثاني! 📚\n'
                'انت/ي خلاص بديت طريقك في الدراسة، عشان نضيفك للمجموعة، أرسل/ي مباشرة لمشرف المجموعة عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'لو في أي سؤال أو طلب مساعدة، المشرف موجود تواصل/ي معه!'
            )
        if 'ثالث' in processed or 'مستوى ثالث' in processed or 'المستوى الثالث' in processed:
            return (
                'أهلا بيك في المستوى الثالث! 💼\n'
                'انت/ي أكثر من جاهز/ه للدراسة الجادة! عشان نضيفك للمجموعة، بس أرسل/ي مباشرة لمشرف المجموعة عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'لو محتاج/ه أي مساعدة أو عندك استفسار، المشرف هيساعدك!'
            )
        if 'رابع' in processed or 'مستوى رابع' in processed or 'المستوى الرابع' in processed:
            return (
                'هلا فيك في المستوى الرابع! 🌟\n'
                'انت/ي في مرحلة متقدمة، خلاص قربت توصل للمرحلة النهائية! عشان نضيفك للمجموعة، أرسل/ي مباشرة لمشرف المجموعة عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'أي سؤال أو استفسار؟ تواصل/ي مع المشرف وهو هيساعدك!'
            )
        if 'خامس' in processed or 'مستوى خامس' in processed or 'المستوى الخامس' in processed:
            return (
                'حرفياً انت/ي تستاهل/ي تحية لوصولك المستوى الخامس! 🎓\n'
                'عشان نضيفك للمجموعة، أرسل/ي لمشرف المجموعات، عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'لو في أي شيء حابب تسأل عنه، المشرف هيساعدك!'
            )
        if 'سادس' in processed or 'مستوى سادس' in processed or 'المستوى السادس' in processed:
            return (
                'فخور أنك حالياً في المستوى السادس! 📘\n'
                'عشان نضيفك للمجموعة، أرسل/ي لمشرف المجموعات، عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'لو احتجت أي مساعدة أو عندك سؤال، المشرف موجود عشان يساعدك!'
            )
        if 'سابع' in processed or 'مستوى سابع' in processed or 'المستوى السابع' in processed:
            return (
                'خلاص قربت من النهاية بوصولك للمستوى السابع! 🏆\n'
                'عشان نضيفك للمجموعة، أرسل/ي لمشرف المجموعات، عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'لو في أي شيء حابب تعرفه أو عندك استفسار،المشرف هيساعدك!'
            )
        if 'ثامن' in processed or 'مستوى ثامن' in processed or 'المستوى الثامن' in processed:
            return (
                'مبروك التخرج وصلت المستوى الثامن! 🎓\n'
                'عشان نضيفك للمجموعة، أرسل/ي لمشرف المجموعات، عبر حسابه @m21_001 '
                'الجدول الدراسي واسمك الثنائي من موقع الجامعة (مهم تخفي بياناتك الشخصية غير الضرورية).\n'
                'أي استفسار أو مساعدة؟ تواصل مع المشرف وهو هيساعدك!'
            )
        return ' مافهمتك .. عشان نضيفك للمجموعات لازم مره ثانيه توصلني كلمة "انضمام" وبعدها أعرف مستواك؟ '

    if 'استفسار' in processed or 'سؤال' in processed:
        return (
            'عندك استفسار أو سؤال؟ 🤔\n'
            'اكتب لنا سؤالك في مجموعة المجتمع (@law2students) ، وإذا حابب تواصل مع مشرف المجموعات عشان يجاوبك بشكل أسرع، تقدر/ي تترك/ي له رسالة على حسابه @m21_001 '
            'وهو هيساعدك بأسرع وقت!'
        )

    if 'شكوى' in processed or 'مشكلة' in processed:
        return (
            'يا هلا! 🙋‍♂️ إذا عندك أي مشكلة أو شكوى، احنا مستعدين نساعدك!\n'
            'ارسل لأي مشرف في المجموعات التابعة لـLAW Students  تفاصيل الموضوع، وإذا الموضوع عاجل تواصل/ي مع مشرف المجموعات، على حسابه @m21_001  '
            ''
        )

    if 'اقتراح' in processed:
        return (
            'رائع! 👏 احنا دايمًا مهتمين بملاحظاتك واقتراحاتك علشان نطور الخدمة.\n'
            'أرسل لنا اقتراحك في @law2students، وممكن تتواصل/ي مع مشرف المجموعات بشكل مباشر علشان يناقش معاك أي فكرة @m21_001.'
        )

    return 'المعذرة هذي الرسالة ما تبرمجت أرد عليها😇، تقدر تكلمهم في قروب المناقشة كل طلاب وطالبات كلية الحقوق هناك ومستعدين يساعدونك ومعهم المشرفين جرب ترسل لهم من هنا @law2students 👍🏻، وأنا هنا أقدر أساعدك بس لازم ترسل إحدى الكلمات التالية: انضمام - استفسار - سؤال - شكوى - مشكلة - اقتراح'



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text: str = update.message.text
    user_id: int = update.message.from_user.id

    if user_id not in user_states:
        user_states[user_id] = {}

    response = handle_response(message_text, user_states[user_id])
    await update.message.reply_text(response)

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    application.run_polling()
