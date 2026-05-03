---
title: "4 Ways to Register Spring Bean"
date: 2024-05-25T14:18:07+09:00
slug: "52-Spring-Bean-등록하는-4-가지-방법"
original_url: "https://memoryhub.tistory.com/52"
tistory_id: 52
draft: false
---

# 4 Ways

1. XML - Using Bean tag

2. XML - Using componentScan

3. Bean registration via Config file

4. Bean registration using ComponentScan in Config

---

## **1. XML - Using Bean tag**

### **Create application.xml in Resource folder**

### **application.xml**

```
xml copy
<?xml version="1.0" encoding="UTF-8"?>
<beans ...>
    <bean id="bookService" class="com.springstudy.springapplicationcontext.BookService">
        <property name="bookRepository" ref="bookRepository"/>
    </bean>
    <bean id="bookRepository" class="com.springstudy.springapplicationcontext.BookRepository"/>
</beans>
```

### **Load xml file and run Application**

### **DemoApplication.java**

```
java copy
public class DemoApplication {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
        String[] beanDefinitionNames = context.getBeanDefinitionNames();
        System.out.println(Arrays.toString(beanDefinitionNames)); // print bean name
        BookService bookService = (BookService) context.getBean("bookService");
        System.out.println(bookService.bookRepository != null);
    }
}
```

## **2. XML - Using componentScan**

### **Modify application.xml**

```
xml copy
<?xml version="1.0" encoding="UTF-8"?>
<beans ...>
    <context:component-scan base-package="com.springstudy.springapplicationcontext"/>
</beans>
```

### **Add annotation to Bean Class**

### **BookRepository.java**

```
java copy
@Repository
public class BookRepository {}
```

### **BookService.java**

```
java copy
@Service
public class BookService {
    @Autowired
    BookRepository bookRepository;

    public void setBookRepository(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }
}
```

## **3. Bean registration via Config file**

### **Create ApplicationConfig.java file and create Bean**

### **ApplicationConfig.java**

```
java copy
@Configuration
public class ApplicationConfig {
   @Bean
   public BookRepository bookRepository() {
       return new BookRepository();
   }

   @Bean
   public BookService bookService() {
       BookService bookService = new BookService();
       bookService.setBookRepository(bookRepository());
       return bookService;
   }
}
```

### **Load ApplicationConfig and run Application**

### **DemoApplication.java**

```
java copy
public class DemoApplication {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(ApplicationConfig.class);
        String[] beanDefinitionNames = context.getBeanDefinitionNames();
        System.out.println(Arrays.toString(beanDefinitionNames)); // print bean name
        BookService bookService = (BookService) context.getBean("bookService");
        System.out.println(bookService.bookRepository != null);
    }
}
```

## **4. Bean registration using ComponentScan in Config**

### **ApplicationConfig.java**

```
java copy
@Configuration
@ComponentScan(basePackageClasses = DemoApplication.class)
public class ApplicationConfig {}
```

### **BookService.java**

```
java copy
@Service
public class BookService {
    @Autowired
    BookRepository bookRepository;

    public void setBookRepository(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }
}
```

### **DemoApplication.java**

```
java copy
@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```
