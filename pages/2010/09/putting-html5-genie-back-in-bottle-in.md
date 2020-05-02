date: 2010-09-29
published: true
tags: [javascript, security, web standards, html]
title: Putting the HTML5 genie back in the bottle in the name of web security?
updated: 2010-09-29


There's a lot of wisdom in <a href="http://security.sys-con.com/node/1544072">what Crockford continues to say about HTML5 and web security</a>:<br />
<blockquote>The HTML5 proposal does not attempt to correct the XSS problem and actually makes it worse...&nbsp;The fundamental mistake in HTML5 was one of prioritization. It should  have tackled the browser's most important problem first. Once the  platform was secured, then shiny new features could be carefully added.</blockquote>It makes a lot of sense in theory, but I doubted the practicality of it in&nbsp;<a href="http://www.w3.org/QA/2008/12/web_applications_security_requ.html">a Dec 2008 item</a>:<br />
<blockquote>after wrestling with the patchwork of javascript security policies in browsers in the past few weeks, the capability approach in&nbsp;<a href="http://blog.360.yahoo.com/blog-TBPekxc1dLNy5DOloPfzVvFIVOWMB0li?p=706"><span class="Apple-style-span" style="color: black;">adsafe</span></a>&nbsp;looks simple and elegant by comparison. Is there any chance we can move the state-of-the-art that far? ... it seems an impossibly high bar to reach, given the worse-is-better tendency in software deployment...</blockquote>He acknowledges the difficulty, to some extent:<br />
<br />
<blockquote>HTML5 has a lot of momentum and appears to be doomed to succeed.</blockquote><div>Chuckle.</div><div><br />
</div><div>He goes on to recommend to suspend the current HTML5 activity now:</div><blockquote>I think the wiser course is to get it right first. We have learned the hard way that once an error gets into a web standard, it is really hard to get it out.</blockquote><div>Would that standards had so much impact. It's true that once a W3C Working Group is in motion, it's difficult for the organization to decide to stop it. But that's really only tangentially related to the heart of the problem: shipping code. Much of the web development community and many of the users have their fingers on the <a href="http://js1k.com/home">shiny new features</a>; who's going to go first in taking them away?</div>