# iauctb-python
A Python wrapper for [IAUCTB website](http://stu.iauctb.ac.ir).

This wrapper is designed for student's common tasks in [IAUCTB website](http://stu.iauctb.ac.ir), so the readme will be just in Farsi for now!

<h4 dir="rtl">
 توجه : این ماژول درحال توسعه هستش و فعلا  بصورت کامل قابل استفاده نیست!
</h4>

<p dir="rtl">
همونطور که واضح و مبرهنه 
<a href = "http://stu.iauctb.ac.ir">پرتال دانشجویی دانشگاه آزاد اسلامی واحد تهران مرکزی</a>
یکی از داغون ترین طراحی های پرتال تاریخ رو داره و یک انتخاب واحد توش یک روز کامل زمان میبره!
</p>

<p dir="rtl">
این ماژول پایتون طراحی شده که بشه با استفاده ازش فعالیت های مختلف توی سایت رو اوتوماتیک انجام داد. مثل لیست کردن نمرات یا حتی انتخاب واحد.
</p>

<p dir="rtl">
برای استفاده از این ماژول به پایتون نسخه ی ۳ و کتابخانه Selenium نیاز هستش. همینطور لازم هست که فعلا از سیتسم عامل ویندوز استفاده نکنید. و همینطور فایرفاکس هم روی سیستمتون نصب باشه.
</p>

<h2 dir="rtl">
راه اندازی
</h2>

<p dir="rtl">
ابتدا باید کتابخونه Selenium را نصب کنید.
</p>
` pip3 install selenium `

<p dir="rtl">
سپس باید فایل 
<a href="https://github.com/sinabakh/iauctb-python/blob/master/config.py">config.py</a>
را تغییر داده و اطلاعات کاربری خود را وارد کنید و درنهایت همه چیز آماده می باشد.
</p>

<p dir="rtl">
حال میتوانید کد خود رابزنید یا از 
<a href="https://github.com/sinabakh/iauctb-python/blob/master/demo.py">demo.py</a>
استفاده کنید!
</p>

<h2 dir="rtl">
سوالات متداول
</h2>
<h4 dir="rtl">
چرا پایتون ۳ ؟
</h4>
<p dir="rtl">
با این که پایتون ۲ دارای ساپورت بیش تری از کتابخونه هاست اما چون در این پروژه به شدت از نوشته های فارسی استفاده میشود و پایتون ۲ با نوشته های UTF مشکل دارد پس از پایتون ۳ استفاده شده است.
</p>

<h4 dir="rtl">
فایرفاکس ؟
</h4>
<p dir="rtl">
اگه کد رو یکبار اجرا کنید میبینید که یک پنجره فایرفامس برای شما باز میشود و بصورت خودکار یک سری کار انجام میدهد.
دلیل انتخاب فایرفاکس اینه که پروسه ی تست راحت تر باشه.
اما درنهایت این ماژول به Phantomjs که از محیط گرافیکی استفاده نمیکند کوچ خواهد کرد.
</p>

<h2 dir="rtl">
مجوز
</h2>
```
DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
