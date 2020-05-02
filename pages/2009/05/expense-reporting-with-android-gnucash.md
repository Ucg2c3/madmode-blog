date: 2009-05-05
published: true
tags: [mobile, travel, SFO, 'free culture', finances, android, business, america]
title: Expense reporting with Android, GnuCash, and IRS.gov
updated: 2010-06-02


Getting a new <a href="http://www.amazon.com/gp/feature.html/ref=amb_link_83669991_1?ie=UTF8&amp;docId=1000323301&amp;pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=auto-sparkle&amp;pf_rd_r=1PSHGV2T63V1B6ANGM20&amp;pf_rd_t=301&amp;pf_rd_p=469746031&amp;pf_rd_i=g1">G1 T-Mobile Google cell phone</a> is an investment in the <a href="http://en.wikipedia.org/wiki/Google_Android">android platform</a>, which isn't yet mature. It's like getting a new puppy: it's cute but it pees on the floor sometimes. You can install all sorts of applications, but each one involves a little training.<br />
<br />
I took it on two trips to San Francisco in March: one for a meeting of the&nbsp; <a href="http://www.w3.org/2001/tag/">W3C Technical Architecture Group</a> hosted by Oracle and one for the 74th <a href="http://www.ietf.org/">IETF</a> meeting.<br />
<br />
I know, after years of painful experience, how <a href="http://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology">MIT</a> handles expense reporting. But MIT employs only half of me <a href="http://lists.w3.org/Archives/Public/public-html/2008Oct/0087.html">now</a>. How should Midwest Web Sense handle travel expense <a href="http://en.wikipedia.org/wiki/Financial_statements">accounting</a>?<br />
<br />
<a name='more'></a><br />
<br />
<a href="http://www.cyrket.com/package/com.tf"><img align="right" alt="" height="64" src="http://ne.edgecastcdn.net/8003A4/www.cyrket.com/image/-5583491875389410109" title="Receipt Filer Lite" width="64" /></a>I took pictures of all my receipts from the IETF trip using <a href="http://www.cyrket.com/package/com.tf">Receipt Filer Lite</a> on the android. It has fields for amount, category (transportation, restaurant, food), business name.&nbsp; The camera integration is great, but the only way I can see to get the data out is email, one at a time. It's missing bulk export, let alone two way synchronization with the cloud.<br />
<br />
This comes as something of a shock to a long-time <a href="http://en.wikipedia.org/wiki/Danger_Hiptop">Sidekick</a> user, where everything you tell it is synchronized within seconds. Your gizmo broke while you were drafting a mail message? No problem: get another Sidekick, transfer your SIM card, and presto, it syncs with the cloud and there's your draft waiting for you.<br />
<br />
That brings us to another lesson I leaned from years of painful experience: using a computer to capture your knowledge is only better than paper once you've got a second copy on another machine. Back it up, email it, commit it to a <a href="http://en.wikipedia.org/wiki/Revision_control">source code control system</a>, or synchronize it; but be wary of the promise that first machine gives you when you press "save".<br />
<br />
Jacob Nielsen has been spelling out <a href="http://www.useit.com/alertbox/20020526.html">the requirement for automatic sync</a> since at least as far back as May 2002, so I find it a little obnoxious that the Google engineers act like they thought it up in their <a href="http://googlemobile.blogspot.com/2008/10/google-on-android-gmail-and-contacts.html">Oct 2008 piece</a>:<br />
<blockquote>"It occurred to us that the best way to synchronize these various pieces of information is to let the device do it on its own while you're not looking, so you never have to think about it."</blockquote><br />
To be fair, the built-in personal information applications do sync to the cloud, and the google calendar web application is orders of magnitude faster than T-Mobile's adware-bloated "desktop interface". The android platform is quite open, and with openness comes more freedom to do things poorly as well as more freedom to do things well.<br />
<br />
<a href="http://www.gnucash.org/"><img align="right" alt="" height="45" src="https://www.gnucash.org/externals/banner5.png" title="GnuCash" width="453" /></a>The <a href="http://www.gnucash.org/">GnuCash project</a> is the open source answer to the Quicken/Microsoft Money application space. I'm happy to say that budgeting and other requirements that I found unmet in previous releases are now supported and the overall feel is quite mature, right down to the documentation. I see a few memo fields that didn't survive migration from my Quicken records via <a href="http://en.wikipedia.org/wiki/Quicken_Interchange_Format">QIF</a> export, but all the balances are intact.<br />
<br />
I hadn't really thought through the expense accounts (called "categories" in Quicken-speak) since opening checking and credit card accounts for Midwest Web Sense. I'm assuming that we won't have trouble with the IRS no matter how poorly we did the 2008 tax return, since the business was clearly in the red no matter how you slice it. So we have until the next tax season to get this right, so I'm doing a little bit of my own research rather than hire an accountant right away.<br />
<br />
<a href="http://www.irs.gov/businesses/small/index.html"><img align="right" alt="IRS" height="72" src="https://www.irs.gov/irs/cda/common/images/irslogo.gif" title="IRS" width="354" /></a><br />
I cringed at the first recommendation that I try the <a href="http://www.irs.gov/">IRS web site</a>, but by the 3rd or 4th recommendation, I did give it a try, and I'm happy to say that it's reasonably good. For example, section 8.                                    &nbsp;                                  <a href="http://www.irs.gov/publications/p334/ch08.html">Business Expenses</a> of <em>Publication 334 (2008), Tax Guide for Small Business</em> seems to answer this question about expense accounts; it matches schedule C that we filled out for tax year 2008 quite closely. And <a href="http://www.irs.gov/publications/p535/index.html">Publication 535, Business Expenses</a> answers most questions about travel expense accounting.<br />
<br />
But I can't find anything about whether photocopies are good enough or whether originals are required. And their advice on<a href="http://www.irs.gov/publications/p583/ar02.html#d0e2170"> How Long To Keep Records</a> hardly helps at all:<br />
<blockquote>"You must keep your records as long as they may be needed for the administration of any provision of the Internal Revenue Code. Generally, this means you must keep records that support an item of income or deduction on a return until the period of limitations for that return runs out."</blockquote><br />
Disk and online storage are cheap enough to keep Receipt Filer mail messages forever."Purge files once a year" is the advice from <a href="http://www.minezone.org/wiki/MVance/GettingThingsDone">Getting Things Done</a>. I think I'll try that for my paper records.
