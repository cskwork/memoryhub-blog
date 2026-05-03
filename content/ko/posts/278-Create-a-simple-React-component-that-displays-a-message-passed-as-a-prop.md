---
title: "Create a simple React component that displays a message passed as a prop."
date: 2024-06-12T00:37:17+09:00
slug: "278-Create-a-simple-React-component-that-displays-a-message-passed-as-a-prop"
original_url: "https://memoryhub.tistory.com/278"
tistory_id: 278
draft: false
categories: ["데브 라이브러리"]
tags: ["React"]
---

*In this response, I'll guide you through creating a simple React component that displays a message passed as a prop, breaking down each step with an analogy to make the process clear and understandable.*

### The Big Picture

Imagine you're building a small sign that can display different messages. The message on the sign can be changed by providing a new message. In React, we create components to build our UI, similar to constructing different parts of a sign. Here, we'll create a component that takes a message as an input (prop) and displays it.

### Core Concepts

1. **Component**: A reusable piece of UI. Think of it like a blueprint for a part of the sign.
2. **Props**: Short for properties, these are inputs to components. They are like the text we write on the sign.
3. **JSX**: A syntax extension for JavaScript that looks similar to HTML and is used to describe what the UI should look like.

### Detailed Walkthrough

1. **Setting Up the Environment**: Make sure you have Node.js and npm (Node Package Manager) installed. Create a new React project using Create React App.
2. **Creating the Component**: Define a new function that represents the component.
3. **Using Props**: Pass the message as a prop to the component.
4. **Rendering the Component**: Use JSX to display the message.

### Understanding Through an Example

1. **Setting Up the Environment**:

   - Open your terminal.
   - Run the following commands to create a new React project:

     ```
     npx create-react-app my-app
     cd my-app
     npm start
     ```

     This will start a new React project and open it in your browser.
2. **Creating the Component**:

   - Inside the `src` folder, create a new file called `MessageComponent.js`.
   - Add the following code to define your component:

     ```
     import React from 'react';

     const MessageComponent = (props) => {
       return (
           <div>
               {props.message}
           </div>
       );
     };

     export default MessageComponent;
     ```
   - Explanation\*: Here, we import React and define a functional component named `MessageComponent`. This component takes `props` as an argument, which is an object containing the properties passed to it. We then return a JSX element that displays the `message` prop inside a `div`.
3. **Using Props**:

   - Open `src/App.js`.
   - Import your new component and use it inside the App component, passing a message prop to it:

     ```
     import React from 'react';
     import MessageComponent from './MessageComponent';

     function App() {
       return (
           <div className="App">
               <MessageComponent message="Hello, World!" />
           </div>
       );
     }

     export default App;
     ```
   - Explanation\*: We import `MessageComponent` and use it inside the `App` component, passing a `message` prop with the value "Hello, World!". This tells the `MessageComponent` what message to display.
4. **Rendering the Component**:

   - When you save the changes and go to your browser, you should see the message "Hello, World!" displayed on the page.

### Conclusion and Summary

In summary, we created a simple React component that displays a message passed as a prop by:

1. Setting up the environment using Create React App.
2. Creating a new functional component that takes `props` and returns JSX.
3. Using the component in `App.js` and passing a message prop to it.
4. Rendering the component to display the message.

### Test Your Understanding

1. Modify the message prop in `App.js` to display a different message.
2. Create another instance of `MessageComponent` with a different message and display it below the first one.

### Reference

For more detailed information on React components and props, you can refer to the official React documentation: [React Components and Props](https://reactjs.org/docs/components-and-props.html).
