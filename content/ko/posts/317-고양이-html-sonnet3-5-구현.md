---
title: "고양이 html - sonnet3.5 구현"
date: 2024-06-27T12:52:24+09:00
slug: "317-고양이-html-sonnet3-5-구현"
original_url: "https://memoryhub.tistory.com/317"
tistory_id: 317
draft: false
categories: ["데브 라이브러리"]
tags: ["GPT"]
cover:
  image: "/images/317-고양이-html-sonnet3-5-구현/img.png"
  relative: false
  hidden: false
---

![](/images/317-고양이-html-sonnet3-5-구현/img.png)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cute Cat Adventure with Double Jump</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background: linear-gradient(to bottom, #87CEEB, #3CB371);
        }
        #gameCanvas {
            display: block;
        }
        #instructions {
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            font-family: Arial, sans-serif;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas"></canvas>
    <div id="instructions">
        Use arrow keys to move. Press Up to jump, press again for double jump!
    </div>
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const cat = {
            x: canvas.width / 2,
            y: canvas.height - 100,
            width: 60,
            height: 40,
            speed: 5,
            jumpForce: 15,
            gravity: 0.6,
            velocityY: 0,
            velocityX: 0,
            direction: 1,
            isJumping: false,
            doubleJumped: false
        };

        const flowers = [];
        const butterflies = [];

        // Create flowers
        for (let i = 0; i < 20; i++) {
            flowers.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 20 + 10,
                color: `hsl(${Math.random() * 360}, 100%, 50%)`
            });
        }

        // Create butterflies
        for (let i = 0; i < 10; i++) {
            butterflies.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 10 + 5,
                speed: Math.random() * 2 + 1,
                angle: Math.random() * Math.PI * 2
            });
        }

        function drawCat() {
            ctx.save();
            ctx.translate(cat.x + cat.width / 2, cat.y + cat.height / 2);
            ctx.scale(cat.direction, 1);
            ctx.translate(-cat.width / 2, -cat.height / 2);

            // Body
            ctx.fillStyle = 'white';
            ctx.beginPath();
            ctx.ellipse(cat.width / 2, cat.height / 2, cat.width / 3, cat.height / 2, 0, 0, Math.PI * 2);
            ctx.fill();

            // Head
            ctx.beginPath();
            ctx.arc(cat.width * 0.75, cat.height * 0.4, cat.width * 0.2, 0, Math.PI * 2);
            ctx.fill();

            // Eyes
            ctx.fillStyle = 'black';
            ctx.beginPath();
            ctx.arc(cat.width * 0.85, cat.height * 0.3, 3, 0, Math.PI * 2);
            ctx.arc(cat.width * 0.95, cat.height * 0.3, 3, 0, Math.PI * 2);
            ctx.fill();

            // Nose
            ctx.fillStyle = 'pink';
            ctx.beginPath();
            ctx.moveTo(cat.width * 0.9, cat.height * 0.4);
            ctx.lineTo(cat.width * 0.87, cat.height * 0.45);
            ctx.lineTo(cat.width * 0.93, cat.height * 0.45);
            ctx.fill();

            // Ears
            ctx.fillStyle = 'white';
            ctx.beginPath();
            ctx.moveTo(cat.width * 0.7, cat.height * 0.1);
            ctx.lineTo(cat.width * 0.8, cat.height * 0.3);
            ctx.lineTo(cat.width * 0.6, cat.height * 0.3);
            ctx.fill();

            ctx.beginPath();
            ctx.moveTo(cat.width * 0.9, cat.height * 0.1);
            ctx.lineTo(cat.width * 0.8, cat.height * 0.3);
            ctx.lineTo(cat.width, cat.height * 0.3);
            ctx.fill();

            // Legs
            ctx.fillStyle = 'white';
            ctx.fillRect(cat.width * 0.2, cat.height * 0.8, cat.width * 0.15, cat.height * 0.2);
            ctx.fillRect(cat.width * 0.65, cat.height * 0.8, cat.width * 0.15, cat.height * 0.2);

            // Tail
            ctx.beginPath();
            ctx.moveTo(0, cat.height * 0.5);
            ctx.quadraticCurveTo(cat.width * -0.2, cat.height * 0.4, 0, cat.height * 0.3);
            ctx.strokeStyle = 'white';
            ctx.lineWidth = 4;
            ctx.stroke();

            ctx.restore();
        }

        function drawFlowers() {
            flowers.forEach(flower => {
                ctx.fillStyle = flower.color;
                ctx.beginPath();
                for (let i = 0; i < 5; i++) {
                    const angle = (i / 5) * Math.PI * 2;
                    const x = flower.x + Math.cos(angle) * flower.size;
                    const y = flower.y + Math.sin(angle) * flower.size;
                    ctx.lineTo(x, y);
                }
                ctx.closePath();
                ctx.fill();

                ctx.fillStyle = 'yellow';
                ctx.beginPath();
                ctx.arc(flower.x, flower.y, flower.size / 4, 0, Math.PI * 2);
                ctx.fill();
            });
        }

        function drawButterflies() {
            butterflies.forEach(butterfly => {
                ctx.fillStyle = `hsl(${Math.random() * 360}, 100%, 75%)`;
                ctx.beginPath();
                ctx.moveTo(butterfly.x, butterfly.y);
                ctx.lineTo(butterfly.x - 5, butterfly.y + 5);
                ctx.lineTo(butterfly.x + 5, butterfly.y + 5);
                ctx.closePath();
                ctx.fill();

                ctx.beginPath();
                ctx.moveTo(butterfly.x, butterfly.y);
                ctx.lineTo(butterfly.x - 5, butterfly.y - 5);
                ctx.lineTo(butterfly.x + 5, butterfly.y - 5);
                ctx.closePath();
                ctx.fill();
            });
        }

        function updateButterflies() {
            butterflies.forEach(butterfly => {
                butterfly.x += Math.cos(butterfly.angle) * butterfly.speed;
                butterfly.y += Math.sin(butterfly.angle) * butterfly.speed;

                if (butterfly.x < 0 || butterfly.x > canvas.width) butterfly.angle = Math.PI - butterfly.angle;
                if (butterfly.y < 0 || butterfly.y > canvas.height) butterfly.angle = -butterfly.angle;

                butterfly.angle += (Math.random() - 0.5) * 0.1;
            });
        }

        function update() {
            // Horizontal movement
            if (keys.ArrowLeft) {
                cat.velocityX = -cat.speed;
                cat.direction = -1;
            } else if (keys.ArrowRight) {
                cat.velocityX = cat.speed;
                cat.direction = 1;
            } else {
                cat.velocityX *= 0.8; // Friction
            }

            cat.x += cat.velocityX;

            // Jumping
            if (keys.ArrowUp && !keys.ArrowUpPressed) {
                if (!cat.isJumping) {
                    cat.velocityY = -cat.jumpForce;
                    cat.isJumping = true;
                    cat.doubleJumped = false;
                } else if (!cat.doubleJumped) {
                    cat.velocityY = -cat.jumpForce;
                    cat.doubleJumped = true;
                }
                keys.ArrowUpPressed = true;
            }

            // Apply gravity
            cat.velocityY += cat.gravity;
            cat.y += cat.velocityY;

            // Ground collision
            if (cat.y + cat.height > canvas.height) {
                cat.y = canvas.height - cat.height;
                cat.velocityY = 0;
                cat.isJumping = false;
                cat.doubleJumped = false;
            }

            // Screen boundaries
            if (cat.x < 0) cat.x = 0;
            if (cat.x + cat.width > canvas.width) cat.x = canvas.width - cat.width;

            updateButterflies();
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawFlowers();
            drawButterflies();
            drawCat();
        }

        function gameLoop() {
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }

        const keys = {
            ArrowUpPressed: false
        };

        document.addEventListener('keydown', (e) => {
            keys[e.code] = true;
        });

        document.addEventListener('keyup', (e) => {
            keys[e.code] = false;
            if (e.code === 'ArrowUp') {
                keys.ArrowUpPressed = false;
            }
        });

        gameLoop();
    </script>
</body>
</html>
```
