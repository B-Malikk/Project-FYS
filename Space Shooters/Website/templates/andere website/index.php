<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title> Space Shooters </title>
  <link rel="stylesheet" href="Login_Space_shooters.css">

</head>

<body>
  <div class="box">
    <h2>Create account</h2>
    <form action="config.php" method="post">
      <div class="input-box">
        <input type="text" name="username" autocomplete="off" required>
        <label for="">Username</label>
      </div>
      <div class="input-box">
        <input type="email" name="email" autocomplete="off" required>
        <label for="">Email</label>
      </div>
      <div class="input-box">
        <input type="password" name="password" autocomplete="off" required>
        <label for="">Password</label>
      </div>
      <input type="submit" value="Let the journey begin !">
    </form>
  </div>
</body>

</html>