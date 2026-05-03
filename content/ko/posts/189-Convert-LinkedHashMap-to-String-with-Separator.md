---
title: "Convert LinkedHashMap to String with Separator"
date: 2024-06-04T12:41:09+09:00
slug: "189-Convert-LinkedHashMap-to-String-with-Separator"
original_url: "https://memoryhub.tistory.com/189"
tistory_id: 189
draft: false
---

Here's how you can convert the linked hashmap into a single string separated by underscores using Java:

```
import java.util.LinkedHashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Create the LinkedHashMap and populate it with the given values
        LinkedHashMap<String, String> map = new LinkedHashMap<>();
        map.put("triggerIdx", "IDX");
        map.put("keywords", "스톤헨지");
        map.put("category", "돌");

        // Check if the map is empty and handle accordingly
        if (map.isEmpty()) {
            System.out.println("The map is empty.");
            return;
        }

        // Initialize a StringBuilder to construct the result string
        StringBuilder result = new StringBuilder();

        // Iterate through the map and append key-value pairs to the result
        for (Map.Entry<String, String> entry : map.entrySet()) {
            if (result.length() > 0) {
                result.append("_");
            }
            result.append(entry.getKey()).append("_").append(entry.getValue());
        }

        // Convert StringBuilder to String and print the result
        String finalString = result.toString();
        System.out.println(finalString);
    }
}
```

### Explanation

1. **Create and Populate LinkedHashMap:**

   - A `LinkedHashMap` is created and populated with the given key-value pairs to maintain the insertion order.
2. **StringBuilder Initialization:**

   - A `StringBuilder` is used to efficiently build the result string.
3. **Iterate Through the Map:**

   - The code iterates through the entries of the map. For each entry, it appends the key and value to the `StringBuilder`, separated by an underscore. If the `StringBuilder` already contains some text, an additional underscore is added before appending the new key-value pair.
4. **Convert to String and Print:**

   - The `StringBuilder` content is converted to a `String`, which is then printed.

When you run this Java code, it will output:

```
triggerIdx_IDX_keywords_스톤헨지_category_돌
```
