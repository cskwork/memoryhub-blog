---
title: "Spring Bean 등록하는 4 가지 방법"
date: 2024-05-25T14:18:07+09:00
slug: "52-Spring-Bean-등록하는-4-가지-방법"
original_url: "https://memoryhub.tistory.com/52"
tistory_id: 52
draft: false
---

# 4 가지 방법

1. xml - Bean 태그 이용

2. XML - componentScan 사용

3. Config파일을 통한 Bean 등록

4. Config의 ComponentScan을 활용한 Bean 등록

---

## **1. xml - Bean 태그 이용**

### **Resource 폴더에 application.xml 생성**

### **application.xml**

```
xml코드 복사
<?xml version="1.0" encoding="UTF-8"?>
<beans ...>
    <bean id="bookService" class="com.springstudy.springapplicationcontext.BookService">
        <property name="bookRepository" ref="bookRepository"/>
    </bean>
    <bean id="bookRepository" class="com.springstudy.springapplicationcontext.BookRepository"/>
</beans>
```

### **xml 파일을 로드하여 Application 실행**

### **DemoApplication.java**

```
java코드 복사
public class DemoApplication {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
        String[] beanDefinitionNames = context.getBeanDefinitionNames();
        System.out.println(Arrays.toString(beanDefinitionNames)); // bean name 출력
        BookService bookService = (BookService) context.getBean("bookService");
        System.out.println(bookService.bookRepository != null);
    }
}
```

## **2. XML - componentScan 사용**

### **application.xml 수정**

```
xml코드 복사
<?xml version="1.0" encoding="UTF-8"?>
<beans ...>
    <context:component-scan base-package="com.springstudy.springapplicationcontext"/>
</beans>
```

### **Bean Class에 어노테이션 작성**

### **BookRepository.java**

```
java코드 복사
@Repository
public class BookRepository {}
```

### **BookService.java**

```
java코드 복사
@Service
public class BookService {
    @Autowired
    BookRepository bookRepository;

    public void setBookRepository(BookRepository bookRepository) {
        this.bookRepository = bookRepository;
    }
}
```

## **3. Config파일을 통한 Bean 등록**

### **ApplicationConfig.java 파일 생성 및 Bean 생성**

### **ApplicationConfig.java**

```
java코드 복사
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

### **ApplicationConfig를 로드하여 Application 실행**

### **DemoApplication.java**

```
java코드 복사
public class DemoApplication {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(ApplicationConfig.class);
        String[] beanDefinitionNames = context.getBeanDefinitionNames();
        System.out.println(Arrays.toString(beanDefinitionNames)); // bean name 출력
        BookService bookService = (BookService) context.getBean("bookService");
        System.out.println(bookService.bookRepository != null);
    }
}
```

## **4. Config의 ComponentScan을 활용한 Bean 등록**

### **ApplicationConfig.java**

```
java코드 복사
@Configuration
@ComponentScan(basePackageClasses = DemoApplication.class)
public class ApplicationConfig {}
```

### **BookService.java**

```
java코드 복사
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
java코드 복사
@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```
