import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# تفعيل nest_asyncio لتجنب تعارض الحلقات
nest_asyncio.apply()

# دالة لحساب البرج الفلكي بناءً على تاريخ الميلاد
def get_zodiac_sign(day: int, month: int) -> str:
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "برج الحمل", "اليوم مناسب للمغامرة. قد تجد فرصًا جديدة في العمل."
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "برج الثور", "اليوم يوم جيد للتركيز على الأمور المالية. حان الوقت للتخطيط لمستقبل أفضل."
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "برج الجوزاء", "اليوم قد تتلقى أخبارًا مفاجئة. استعد للتعامل مع التغيرات."
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "برج السرطان", "اليوم تشعر بالحاجة إلى الراحة. حاول أن تجد وقتًا للاسترخاء."
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "برج الأسد", "اليوم يوم جيد للتواصل مع الأصدقاء والعائلة. حافظ على الروابط الاجتماعية."
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "برج العذراء", "اليوم يفضل أن تركز على صحتك. قد تجد حوافز جديدة في العمل."
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "برج الميزان", "اليوم قد تجد نفسك وسط صراع داخلي. خذ وقتك في التفكير قبل اتخاذ قرارات هامة."
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "برج العقرب", "اليوم مناسب للتفكير العميق. قد تحصل على بعض الإجابات التي كنت تبحث عنها."
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "برج القوس", "اليوم قد تواجه تحديات في العمل. حافظ على تفاؤلك!"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "برج الجدي", "اليوم يناسبك التخطيط للمستقبل. ابدأ بتحديد أهدافك."
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "برج الدلو", "اليوم قد تشعر بحاجتك إلى التغيير. خذ خطوة جديدة نحو أهدافك."
    else:
        return "برج الحوت", "اليوم تشعر بالإبداع. استمتع باللحظات الجميلة."

# دالة الرد على الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('مرحباً، الرجاء إدخال تاريخ الميلاد بصيغة يوم/شهر.')

# دالة لمعالجة تاريخ الميلاد
async def handle_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    try:
        day, month = map(int, text.split('/'))
        sign, prediction = get_zodiac_sign(day, month)
        await update.message.reply_text(f'برجك هو: {sign}\nتوقعاتك اليوم: {prediction}')
    except ValueError:
        await update.message.reply_text('تاريخ الميلاد غير صالح. الرجاء إدخاله بالصورة الصحيحة (يوم/شهر).')

# الدالة الرئيسية
async def main() -> None:
    application = ApplicationBuilder().token("6624505027:AAHYhnp8p2U8Y7CodMb70E3sSVekWvYodv4").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_birthday))
    await application.run_polling()

# استخدام حلقة الأحداث المناسبة
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())  # تشغيل الوظيفة الرئيسية باستخدام run_until_complete
