---
title: "How to Navigate from Java Service Interface Methods to MyBatis XML Tags in IntelliJ"
date: 2025-03-26T16:00:21+09:00
slug: "531-IntelliJ에서-Java-서비스-인터페이스-메서드에서-MyBatis-XML-태그로-이동하는-방법"
original_url: "https://memoryhub.tistory.com/531"
tistory_id: 531
draft: false
---

In IntelliJ IDEA, there are several ways to easily navigate from Java service interface methods to mapped MyBatis XML tags. The most effective method is using the MyBatis plugin, which allows bidirectional navigation between methods and XML tags.

## Main Solutions

1. **Install MyBatis Plugin**
2. **Use Ctrl+Alt+B or Ctrl+Shift+Alt+B Shortcut**
3. **Right-click on Interface Method and Select "Go to Declaration"**
4. **Annotation-based Navigation**

## Detailed Explanation

### 1. MyBatis Plugin Installation and Usage

The MyBatis plugin is the most effective way to provide navigation between Java interfaces and MyBatis XML mappings in IntelliJ IDEA.

```
File > Settings > Plugins > Marketplace > Search 'MyBatis' > Install
```

Main plugins available for installation:

- Free MyBatis Plugin
- MyBatisX

Once these plugins are installed, the following features are provided:

- Bidirectional navigation between interface methods and corresponding XML tags
- Code completion and auto-generation
- Validation of match between method names and XML IDs

### 2. Navigation via Shortcuts

After installing the MyBatis plugin:

- Position your cursor on an interface method and press `Ctrl+Alt+B` or `Ctrl+Shift+Alt+B` shortcut.
- Options to navigate directly to mapped XML tags will be displayed.

### 3. Using Context Menu

1. Position cursor on interface method and right-click
2. Select "Go to Declaration" or "Go to Implementation(s)"
3. Navigate to the MyBatis XML tag mapped to the interface method

### 4. Annotation-based Navigation

When using MyBatis mapper annotations:

```
@Mapper
public interface UserMapper {
    @Select("SELECT * FROM users WHERE id = #{id}")
    User getUserById(Long id);
}
```

In this case, clicking the annotation or pressing `Ctrl+B` will navigate directly to the corresponding SQL query.

### 5. Configuration File Settings

Make sure your MyBatis configuration is set up correctly:

- Verify that the `mybatis-config.xml` file is correctly configured
- Ensure that mapper XML files are in the correct path
- Verify that namespace and IDs exactly match the interface and method names

## Troubleshooting When Errors Occur

1. **Reinstall Plugin**: Try removing and reinstalling the plugin.
2. **Clear Cache**: Select `File > Invalidate Caches / Restart`
3. **Restart Project**: Restart IntelliJ or reload the project.
4. **Verify Mapping**: Check that the interface namespace and XML file namespace are identical.

## Conclusion

Using the MyBatis plugin in IntelliJ IDEA allows you to easily navigate from Java service interface methods to mapped XML tags. This improves development productivity and makes code exploration easier.
