<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Anusha | Portfolio</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(to right, #1f4037, #99f2c8);
      color: #fff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      overflow: hidden;
    }
    h1 {
      font-size: 3rem;
      margin-bottom: 10px;
    }
    p {
      font-size: 1.2rem;
      color: #eee;
      margin-bottom: 20px;
    }
    button {
      padding: 12px 25px;
      background-color: #fff;
      color: #1f4037;
      border: none;
      border-radius: 25px;
      font-size: 1rem;
      cursor: pointer;
    }
    button:hover {
      background-color: #f0f0f0;
    }
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
</head>
<body>
  <h1>Hello, I'm Praveen</h1>
  <p>Frontend Developer | Intern | Learner</p>
  <button>View Portfolio</button>

  <script>
    gsap.from("h1", { duration: 1, y: -50, opacity: 0, ease: "bounce" });
    gsap.from("p", { duration: 1, x: -100, opacity: 0, delay: 0.5 });
    gsap.from("button", { duration: 1, scale: 0, opacity: 0, delay: 1 });
  </script>
</body>
</html>
