---
id: WS-C14-005
title: Services as an Attack Vector
source_pages: "168-170"
chapter: 14
concepts: [third-party-javascript, browser-sandbox, malvertising, exploit-kits, payload, ad-platform, safeframe, iframe-sandbox, ad-review, web-components]
related: [WS-C14-004, WS-C14-006, WS-C12-005, WS-C03-003]
time_sensitive: true
---
# Services as an Attack Vector
(Source: PDF pp. 168-170, tail PDF p. 171. The section begins at its heading part-way down PDF p. 168; the text above it belongs to WS-C14-004. The tail is the text at the top of PDF p. 171 above the "Summary" heading, which begins WS-C14-006.)

## What the section covers
How services you integrate on the client side can be used to attack your site and its users, with a focus on malvertising and on defences for sites that carry ads (PDF pp. 168-171).

## Meaning
- Third-party services can be a vector for attacks on your site, especially client-side ones, because any JavaScript imported from a third-party domain carries risk (PDF p. 168).
- Example: Google Analytics. You register with Google for a tracking ID and import external JavaScript on the pages you want to track. Listing 14-5 is a script tag whose source is a Google Tag Manager URL carrying your tracking ID (PDF p. 168).
- The imported code can read anything in the page's DOM, including sensitive data users type, and can alter the DOM misleadingly, for example to trick users into entering credentials. Malicious code could come from the service itself or from an attacker who compromised it (PDF p. 168). The book adds that Google Analytics has never been compromised and is used only as an example (PDF p. 169).
- The browser security model is not very sophisticated about third-party client code. JavaScript runs in a sandbox, isolated from the operating system and unable to read files on disk, but all scripts imported from different sources on a page share the same sandbox (PDF p. 169).
- The web components specification, in development by the HTML standards committee at the time of writing, defines finer-grained permissions for code and page elements. Until it is finalized and implemented, apply sensible precautions yourself (PDF p. 169).

## Be wary of malvertising
- Advertising funds much of the web; companies spend over $100 billion a year on online ads. Ad platforms usually place the ads: the site owner (a publisher in ad terms) subscribes and marks areas of the site for ads, and the platform fills them as the page loads using JavaScript imported on each page (PDF p. 169).
- Large platforms such as Google AdSense use analytics about the publisher's content and visitors to decide which ads to show. Publishers may also deal with advertisers directly, or have ad spaces sold on an exchange where buyers purchase blocks of ads (for instance 1,000 impressions aimed at men aged 18-25 who visit sneaker sites) (PDF p. 169).
- Publishers have some control but usually cannot approve each ad beforehand. Google AdSense lets publishers block categories of ads or particular domains, or reject specific ads after they have started appearing (PDF p. 169).
- Risk: attackers often use ad platforms as an attack vector. Malicious ads, called malvertising, let an attacker hit many sites at once with malware. It is an increasingly common threat that embarrasses publishers and ad networks and victimizes their users (PDF p. 169).

## Avoid malware delivery
- Malvertising malware usually arrives through exploit kits, which check whether a browser and operating system are vulnerable before delivering the real malicious code, the payload (PDF p. 169).
- Payloads include scripts that redirect or lock the browser, viruses or ransomware delivered via plug-in vulnerabilities, and JavaScript that mines cryptocurrency in the user's browser (PDF pp. 169-170).
- Exploit kit authors are in an arms race with researchers: kits live at dynamically generated URLs, trigger only sporadically to avoid automated scans, and have even been seen detecting virtual machines (which researchers use to quarantine malware) to evade analysis (PDF p. 170).
- If ads on your site hit users with malware, you endanger them. Protect them by partnering only with trustworthy ad platforms, deploying ads in secure frames, and continually watching for malicious ads (PDF p. 170).

### Use a reputable ad platform
- Defending against malvertising is mostly the platform's job: it has the relationship with ad buyers and the cross-advertiser visibility needed to spot bad actors (PDF p. 170).
- Google dominates advertising. Smaller publishers can use the self-service AdSense platform; larger publishers get AdX, which lets them choose ad partners and set their own prices. Both take ads from third-party ad networks (PDF p. 170).
- Because so much of Google's revenue rides on its ad platform, it is "remarkably on the ball" about malicious ads, so make AdSense or AdX your first choice (PDF p. 170).
- Google declines some sites for reputational reasons, for example adult-themed or violent content. Those sites may need a smaller platform with fewer resources and less incentive to protect against malware, so research the platform before picking one (PDF p. 170).

### Use SafeFrame
- The most effective way to isolate third-party content is to host it in an iframe (inline frame) tag. JavaScript inside an iframe cannot access the DOM of the containing page. HTML5 adds the sandbox attribute on iframe, letting the frame specify whether its content may, for example, submit POST requests or open new windows (PDF p. 170).
- The advertising industry adopted SafeFrame, a standard that lets publishers require ads to run in an iframe. It uses iframe tags and adds a JavaScript API that lets advertisers get around some native iframe limitations (PDF p. 170).
- That API lets ad scripts know when the frame is visible and respond to size changes (PDF p. 171).
- Your ad platform should offer an option to show only SafeFrame-compliant ads; choose it. That blocks malicious ad scripts that try to interfere with the page as it renders (PDF p. 171).

### Tailor your ad preferences
- Platforms let you customize the kinds of ads shown. With Google AdSense, show content only from Google certified ad networks, because attackers have bought the expired domains of smaller defunct ad networks to deliver malware (PDF p. 171).
- Consider which categories to block. The book suggests blocking get-rich-quick schemes, multilevel marketing campaigns, and anything describing itself as a downloadable utility (PDF p. 171).

### Review and report suspicious ads
- Periodically review the ads shown on your site in the ad platform dashboard. Ads are tailored per visitor, so just browsing your site will not reveal the whole range (PDF p. 171).
- Report and block anything suspicious. Also log outgoing URLs as users leave your site, to see whether any ads send users to suspicious destinations (PDF p. 171).

## Time-sensitive statements
- Over $100 billion annual online ad spend; Google AdSense and AdX as the dominant platforms; the SafeFrame standard; the web components specification described as upcoming at the time of writing; Google Analytics as the example service.

## Relations
Continues from WS-C14-004 (the other direction of the risk). Recapped in WS-C14-006. Browser JavaScript and sandboxing are covered in Chapter 3 (WS-C03-003).
