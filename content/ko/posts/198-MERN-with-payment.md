---
title: "MERN with payment"
date: 2024-06-06T07:28:28+09:00
slug: "198-MERN-with-payment"
original_url: "https://memoryhub.tistory.com/198"
tistory_id: 198
draft: false
categories: ["데브 유틸"]
tags: ["결제 연동"]
---

*Integrating a payment system into a MERN stack application involves setting up a payment gateway (like Stripe or PayPal) to handle transactions securely.*

### The Big Picture

Imagine you're running an online store built with the MERN stack. To accept payments, you need a way to process credit cards, manage transactions, and ensure everything is secure. A payment gateway is like a virtual cashier that handles all these tasks for you.

### Core Concepts

1. **Payment Gateway**: A service that processes credit card payments and other forms of payment for e-commerce sites.
2. **API Integration**: Using the payment gateway's API to handle payments within your application.
3. **Frontend Handling**: Capturing payment details securely in the frontend.
4. **Backend Processing**: Communicating with the payment gateway and managing transactions in the backend.

### Detailed Walkthrough

1. **Setting Up a Payment Gateway**:

   - **Choose a Payment Gateway**: Stripe and PayPal are popular options.
   - **Create an Account**: Sign up for a developer account on the payment gateway's website.
   - **Obtain API Keys**: Get your public and secret keys for authentication.
2. **Frontend Handling with React**:

   - **Install Payment Gateway SDK**: Add the payment gateway's SDK to your React application.
   - **Securely Capture Payment Details**: Use the SDK to create a payment form that securely captures and tokenizes payment details.

   Example with Stripe:

   ```
   npm install @stripe/stripe-js
   npm install @stripe/react-stripe-js
   ```

   ```
   // PaymentForm.js
   import React from 'react';
   import { loadStripe } from '@stripe/stripe-js';
   import { Elements, CardElement, useStripe, useElements } from '@stripe/react-stripe-js';

   const stripePromise = loadStripe('your-public-key');

   const PaymentForm = () => {
       const stripe = useStripe();
       const elements = useElements();

       const handleSubmit = async (event) => {
           event.preventDefault();
           if (!stripe || !elements) return;

           const card = elements.getElement(CardElement);
           const result = await stripe.createToken(card);

           if (result.error) {
               console.error(result.error.message);
           } else {
               console.log(result.token);
               // Send token to your server
           }
       };

       return (
           <form onSubmit={handleSubmit}>
               <CardElement />
               <button type="submit" disabled={!stripe}>Pay</button>
           </form>
       );
   };

   const App = () => (
       <Elements stripe={stripePromise}>
           <PaymentForm />
       </Elements>
   );

   export default App;
   ```
3. **Backend Processing with Express**:

   - **Install Payment Gateway SDK**: Add the payment gateway's SDK to your Node.js backend.
   - **Create Payment Endpoint**: Set up an endpoint to handle payment processing.

   Example with Stripe:

   ```
   npm install stripe
   ```

   ```
   // server.js
   const express = require('express');
   const Stripe = require('stripe');
   const bodyParser = require('body-parser');

   const app = express();
   const stripe = Stripe('your-secret-key');

   app.use(bodyParser.json());

   app.post('/pay', async (req, res) => {
       const { token, amount } = req.body;
       try {
           const charge = await stripe.charges.create({
               amount,
               currency: 'usd',
               source: token.id,
               description: 'Test Charge',
           });
           res.json(charge);
       } catch (error) {
           res.status(500).send(error);
       }
   });

   app.listen(3000, () => console.log('Server running on port 3000'));
   ```
4. **Connecting Frontend and Backend**:

   - **Make API Calls**: Send payment tokens from the frontend to the backend for processing.

   Example:

   ```
   // PaymentForm.js (inside handleSubmit)
   const handleSubmit = async (event) => {
       event.preventDefault();
       if (!stripe || !elements) return;

       const card = elements.getElement(CardElement);
       const result = await stripe.createToken(card);

       if (result.error) {
           console.error(result.error.message);
       } else {
           const response = await fetch('/pay', {
               method: 'POST',
               headers: { 'Content-Type': 'application/json' },
               body: JSON.stringify({ token: result.token, amount: 1000 }), // Amount in cents
           });

           const paymentResult = await response.json();
           console.log(paymentResult);
       }
   };
   ```

### Conclusion and Summary

Integrating a payment system in a MERN stack application involves setting up a payment gateway, securely capturing payment details on the frontend with React, and processing transactions on the backend with Express. This ensures that payments are handled securely and efficiently.

### Test Your Understanding

1. What is the role of a payment gateway in an online application?
2. How do you securely capture payment details in a React application?
3. Why is it important to handle payment processing on the backend?
4. How can you use API keys to authenticate payment requests?

### Reference

- [Stripe Documentation](https://stripe.com/docs)
- [PayPal Developer](https://developer.paypal.com/docs/checkout/)
