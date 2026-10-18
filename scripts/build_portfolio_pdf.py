from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[1];OUT=R/'docs/Madina_Development_Portfolio_RU.pdf'
for name,file in [('sans','DejaVuSans.ttf'),('bold','DejaVuSans-Bold.ttf'),('serif','DejaVuSerif.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
W,H=960,540; bg='#F6F3ED';ink='#202820';muted='#62675E';gold='#9C7948';green='#17251F';pale='#D3D9CC'; c=canvas.Canvas(str(OUT),pagesize=(W,H));c.setTitle('Мадина Дахкилгова — Портфолио разработчика');c.setAuthor('Madina Dakhkilgova');c.setSubject('Frontend, AI products and automation. Updated 18 October 2026.')
def text(s,x,y,size=17,font='sans',color=ink):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,H-y-size*.82,s)
def lines(s,x,y,width,size=17,leading=26,font='sans',color=ink):
 for para in s.split('\n'):
  words=para.split();line=''
  for word in words:
   t=(line+' '+word).strip()
   if pdfmetrics.stringWidth(t,font,size)>width and line:text(line,x,y,size,font,color);y+=leading;line=word
   else:line=t
  if line:text(line,x,y,size,font,color);y+=leading
  else:y+=leading*.4
 return y
def rule(y,x=48,w=864,color='#D6D9CF'):
 c.setStrokeColor(HexColor(color));c.setLineWidth(.7);c.line(x,H-y,x+w,H-y)
def page(n,label,dark=False):
 col=green if dark else bg;c.setFillColor(HexColor(col));c.rect(0,0,W,H,fill=1,stroke=0)
 text(label.upper(),48,32,10,'sans',pale if dark else gold)
 rule(500,color='#415047' if dark else '#D6D9CF');text('MADINA DAKHKILGOVA  /  DEVELOPMENT',48,514,8,'sans',pale if dark else muted);text(f'{n:02d} / 11',865,514,8,'sans',pale if dark else muted)
def link(label,url,x,y,color=green,size=12):
 text(label,x,y,size,'sans',color);tw=pdfmetrics.stringWidth(label,'sans',size);c.setStrokeColor(HexColor(color));c.setLineWidth(.5);c.line(x,H-y-size-3,x+tw,H-y-size-3);c.linkURL(url,(x,H-y-size-6,x+tw,H-y+3),relative=0,thickness=0)
def img(path,x,y,w,h):
 im=Image.open(path);iw,ih=im.size;scale=min(w/iw,h/ih);a,b=iw*scale,ih*scale;c.drawImage(str(path),x+(w-a)/2,H-y-b,a,b,mask='auto')
def done():c.showPage()
site='https://madina-portfolio-sage.vercel.app/';creator='https://madina-di.github.io/sofiere-studio/'
page(1,'Портфолио разработчика / октябрь 2026',True)
text('Мадина',48,102,58,'serif',bg);text('Дахкилгова',48,169,58,'serif',bg)
text('Frontend Developer',51,278,24,'sans',bg);text('& AI Product Builder',51,313,24,'sans',bg)
lines('Веб-приложения, бизнес-системы\nи автоматизация',52,382,670,18,28,color=pale)
link('madina-portfolio-sage.vercel.app',site,52,456,pale,12)
text('MD',730,166,79,'serif','#A2AE97');text('DESIGN',755,294,10,'sans',pale);text('DEVELOPMENT',755,316,10,'sans',pale);text('PRODUCT',755,338,10,'sans',pale)
done()
page(2,'Профиль и опыт')
lines('Приложения с пониманием\nбизнес-процессов',48,82,840,36,46,'serif')
lines('Разрабатываю интерфейсы и продуктовую логику, подключаю API и автоматизирую повторяющуюся работу. Использую AI в разработке и проверяю результат через тесты и практические сценарии.',48,207,840,18,28)
rule(320)
text('ПРОФЕССИОНАЛЬНАЯ БАЗА',48,344,10,'bold',gold);lines('Финансы и кредит\nБухгалтерия и строительные процессы',48,377,395,18,28)
text('ОБУЧЕНИЕ И ПРАКТИКА',505,344,10,'bold',gold);lines('Skillfactory: frontend, 2025\nCalArts / Coursera: UX/UI, 2026\nfreeCodeCamp: Responsive Web Design',505,377,405,16,27)
done()
page(3,'01 / Sofidar',True)
text('Sofidar',48,82,48,'serif',bg)
lines('AI-платформа\nдля фото и видео',48,155,480,28,38,'sans',bg)
lines('Проектирую продуктовый путь, интерфейс и интеграции: от брифа и раскадровки до генерации сцен и сохранения результата.',48,260,470,18,28,color=pale)
lines('Next.js, React, TypeScript\nPrisma, PostgreSQL, AI API\nОчередь задач, кредиты и платёжные сценарии',48,364,470,14,22,color=pale)
for j,t in enumerate(['Проекты','Генерация','Тренды','Обучение']):
 text(f'0{j+1}',604,146+j*70,10,'sans','#BDAB86');text(t,652,139+j*70,26,'serif',bg)
text('Опубликована и активно развивается',48,455,12,'sans',pale);link('sofidar.com','https://sofidar.com/',650,455,pale,13)
done()
page(4,'02 / Stroyka CRM')
text('Stroyka CRM',48,80,45,'serif');lines('Операционный и финансовый учёт\nстроительных проектов',48,150,840,25,34)
lines('Продуктовая модель основана на моём опыте работы в строительной бухгалтерии. Бюджет объекта, сумма договора и фактические платежи учитываются раздельно.',48,244,450,18,28)
for j,t in enumerate(['Контрагенты','Объекты','Договоры','Платежи']):
 text(f'0{j+1}',593,239+j*43,11,'sans',gold);text(t,637,231+j*43,24,'serif')
lines('Next.js, React, Prisma, PostgreSQL, Zod\nОбщая валидация форм и API, unit- и integration-тесты',48,387,840,14,23,color=muted)
text('Приватный продукт в разработке. Демонстрация по запросу.',48,452,12,'sans',muted);link('Открыть кейс',site+'case-crm.html',790,451,size=12)
done()
page(5,'03 / Card Studio')
text('Card Studio',48,78,43,'serif');text('Подготовка карточек Wildberries',48,137,22)
lines('Версия 2: импорт таблиц и карточек из кабинета WB, характеристики по справочникам, AI-тексты по фактам товара и согласование по ссылке.',48,206,385,17,26)
lines('Создание и обновление через официальный API. Очередь задач и проверка результата отправки.',48,336,385,17,26)
img(R/'image/card-studio-v2-catalog.jpg',465,190,445,260)
text('Демо-магазин с учебными товарами',480,443,10,'sans',muted)
text('Next.js / TypeScript / SQLite / WB Content API',48,422,12,'sans',muted)
text('Сервис опубликован. Первый клиентский пилот впереди.',48,468,11,'sans',muted);link('Сайт сервиса','https://card-studio-production.up.railway.app',770,468,size=11)
done()
page(6,'04 / Obmer',True)
text('Obmer',48,82,48,'serif',bg);lines('Обмер помещений\nс LiDAR',48,153,465,30,40,'sans',bg)
lines('iOS-приложение для дизайнеров интерьеров. Сканирование помещений, ручные замеры, проверка качества и экспорт результатов.',48,270,465,18,28,color=pale)
lines('Swift, SwiftUI, ARKit, RoomPlan\nПродукт в разработке. Нужен iPhone или iPad с LiDAR.',48,397,470,14,23,color=pale)
text('iOS',615,147,70,'serif',bg);text('LiDAR',615,229,52,'serif',bg);text('USDZ / JSON / OBJ',619,327,16,'sans',pale)
link('Кейс проекта',site+'case-obmer.html',620,451,pale,12);link('GitHub','https://github.com/Madina-DI/Obmer',782,451,pale,12)
done()
page(7,'Автоматизация')
text('Контентные системы и боты',48,81,35,'serif');text('Система публикаций: работает, закрытый доступ. DI Translator: прототип.',48,130,11,'sans',muted)
text('AI Social Publishing Manager',48,166,21,'bold');text('Telegram-продукты',530,166,21,'bold')
lines('Система управления публикациями из GPT: очередь, согласование, расписание, проверка медиа и публикация через Meta API.',48,220,390,17,27)
lines('Oberezhno: сообщения по расписанию, подписчики и сценарии ответов.\nDI Translator: AI-переводчик с polling и webhook.',530,220,380,17,27)
lines('Node.js, Railway, Drive, Sheets\nЖурнал публикаций и защита от дублей',48,369,390,14,23,color=muted)
lines('Node.js, Telegram API\nSupabase, Telegraf, Express',530,369,380,14,23,color=muted)
link('Кейс системы публикаций',site+'case-social-manager.html',48,454,size=12);link('Oberezhno',site+'case-oberezhno.html',530,454,size=12);link('DI Translator','https://github.com/Madina-DI/Di-translatorai-bot',700,454,size=12)
done()
page(8,'Интерактивный web',True)
text('Dost',48,82,51,'serif',bg);lines('3D-сайт\nдля AI-компании',48,159,450,31,41,'sans',bg)
lines('Сцена работает прямо в браузере: интерактивные объекты, отражения, шейдерные эффекты, несколько языков и озвучка.',48,282,460,18,29,color=pale)
text('Three.js',616,146,39,'serif',bg);text('WebGL',616,212,39,'serif',bg);text('GLSL',616,278,39,'serif',bg)
text('Опубликован. Интерфейс и браузерная графика.',48,413,13,'sans',pale)
link('Открыть сайт','https://madina-di.github.io/dostik-site-3d/',48,454,pale,12);link('GitHub','https://github.com/Madina-DI/dostik-site-3d',233,454,pale,12)
done()
page(9,'Frontend-практика')
text('Учебные проекты',48,76,39,'serif');text('Завершённые учебные работы с опубликованными демо',48,130,12,'sans',muted)
img(R/'image/kanban-preview.jpg',48,157,410,219);img(R/'image/previewBookshop.jpg',514,157,398,219)
text('Kanban Board',48,389,22,'bold');text('Bookshop',514,389,22,'bold')
text('React / Router / localStorage',48,426,14,'sans',muted);text('JavaScript / SCSS / API',514,426,14,'sans',muted)
link('Демо','https://kanban-board-one-inky.vercel.app',48,463,size=12);link('Демо','https://madina-di.github.io/Bookshop/',514,463,size=12)
text('Также: YOUTalk, JavaScript Slider, Product Landing',154,464,11,'sans',muted)
done()
page(10,'Навыки')
text('Технологии и подход',48,81,39,'serif')
rows=[('Frontend','JavaScript, TypeScript, React, Next.js, HTML, CSS/SCSS'),('Backend и данные','Node.js, PostgreSQL, Prisma, SQLite, REST API'),('Качество и процесс','Git/GitHub, Zod, unit/integration tests, Playwright'),('Интерфейсы и платформы','Figma, UX/UI, Swift/SwiftUI, Three.js')]
for i,(a,b) in enumerate(rows):
 y=172+i*67;text(a,48,y,15,'bold');text(b,335,y,15);rule(y+40)
lines('Продуктовая логика, интерфейс и интеграции. AI-assisted development с проверкой результата.',48,449,860,14,22,color=muted)
done()
page(11,'Контакты')
lines('Обсудим ваш продукт\nили автоматизацию',48,80,850,39,49,'serif')
link('Сайт-портфолио разработчика',site,48,234,size=18)
link('madinadakhkilgova3@gmail.com','mailto:madinadakhkilgova3@gmail.com',48,288,size=16)
link('Telegram: @madina_mi','https://t.me/madina_mi',48,333,size=16)
link('WhatsApp: +1 (916) 225-0794','https://wa.me/19162250794',48,377,size=16)
text('ДРУГОЕ НАПРАВЛЕНИЕ',626,238,10,'bold',gold);text('Sofiere Studio',626,273,24,'serif')
lines('AI-фильмы и визуальные\nистории для брендов',626,318,280,16,25,color=muted)
link('Портфолио AI-креатора',creator,626,400,size=14)
text('Удалённая работа и проектное сотрудничество',48,459,13,'sans',muted)
done();c.save()
print(str(OUT), '11 pages', OUT.stat().st_size, 'bytes')
