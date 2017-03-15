# Flask URL Shortener

A python Flask and MySQL based URL shortening project that I built for personal use. You can try out and play with the deployed version at **[Sh.ubham.com/shorten](http://Sh.ubham.com/shorten).**

## Some key Features
### Ability to change short URL destinations without Login
 I required that my URL shortener posses the ability to change URL destinations without having the need of a login or creating an account of any type an consequently I opted with the mechanism where along with the **short URL** another URL called the **change URL** is generated. This URL presents a page which allows the user to change the destination of their short URL as many times as required without any need for authentication.

This change URL is only presented once to the user during the short URL creation process. If the user fails to save or Bookmark the Change URL then it is lost forever and can not be retrieved again. So the user also looses the ability to change the destination of their shortened URL.

### Security aspects of the "Change URL" mechanism
* The change URL is randomly chosen among a trillion possibilities and that should prevent any attempts to guess the change URLs.

*  Even if a Change URL is discovered, the Change URL page **doesn't contain any details about which short URL's destination it can modify.** 

* By using a Captcha service such as Google's new Invisible Captcha service on the change pages, the attacks possible by bots trying to guess change page urls can also be prevented.
