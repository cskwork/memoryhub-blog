---
title: "JavaScript Basics 03 - Strict Mode"
date: 2024-05-25T17:57:04+09:00
slug: "82-Javascript-기본-03-엄격-모드"
original_url: "https://memoryhub.tistory.com/82"
tistory_id: 82
draft: false
---

## Summary

- "use strict" in JavaScript was created to prevent backward compatibility issues because the language needed to change and add new features.
- By default, 'use strict' is not applied in browser console, and you need to manually activate it to test code.
- However, when using advanced structures like 'classes' and 'modules', 'use strict' is automatically applied so you don't need to add it to scripts.

## Background of 'use strict'

JavaScript has evolved for quite a long time without compatibility issues because new features were added without changing existing functionality.

This had the advantage that existing code would never break, but it also had the disadvantage that mistakes and incomplete decisions made by JavaScript creators were permanently embedded in the language.

This situation continued until ECMAScript5 (ES5) was introduced in 2009.  
In the newly established ES5, new features were added and some existing features were changed.  
Since existing features were changed, backward compatibility issues could arise. So most changes were designed not to be activated in ES5's default mode.  
Instead, a special directive called "use strict" was used to activate strict mode only when explicitly enabled.

```
"use strict"; // "use strict" must be at the top of the script to be activated

// This entire code runs in a modern way.
...
```

When using browser console to test developed features, 'use strict' is not applied by default.

To use 'use strict' in console, enter 'use strict', press Shift+Enter to line break, then enter desired script.

## Is 'use strict' Really Necessary?

Modern JavaScript provides advanced structures called 'classes' and 'modules'.  
When using these, 'use strict' is automatically applied, so you don't need to add "use strict" to your script.

## Reference

<https://javascript.info/strict-mode>
