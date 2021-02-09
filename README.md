# Design of Responsive Website
## AIM:
To design a responsive website with two break points.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

```
## PROGRAM:
## RESPONSIVE PRODUCTS:

<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>BOOK PUBLISHING COMPANY</title>
</head>

<body>
    <div class="jumbotron jumbotron-fluid" style="background-color: cadetblue;">
        <div class="container text-center">
            <h1 class="display-3">BOOK GALLERY</h1>
            <h5 class="display-6">WE IMPROVE YOUR KNOWLEDGE AND MAKE YOUR FUTURE BRIGHT</h5>
        </div>
    </div>
    <div class="container">
        <div class="row text-center">
            <div class="col-12 col-md-3 "><a href="/Home">Home</a></div>
            <div class="col-12 col-md-3 "><a href="/Fiction">Fiction</a></div>
            <div class="col-12 col-md-3 "><a href="/Classics">Classics</a></div>
            <div class="col-12 col-md-3 "><a href="/Non-Fiction">Non-Fiction</a></div>
        </div>
        <div class="row text-center">
            <div class="col-12">
                <h5 class="display-6">Our Premium Products</h5>
            </div>
        </div>
        <div class="row text-center">
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c1.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">MAN'S SEARCHING FOR MEANING</h5>
                    <p class="card-text">price: Rs.300.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c2.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">SAPIENS</h5>
                    <p class="card-text">price: Rs.500.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c3.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">THE ALCHEMIST </h5>
                    <p class="card-text">price: Rs.200.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c4.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">THE SILENT PATIENT</h5>
                    <p class="card-text">price: Rs.300.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c5.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">THE POWER OF YOUR SUBCONSCIOUS MIND</h5>
                    <p class="card-text">price: Rs.300.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c6.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">A GENTLEMAN IN MOSCOW</h5>
                    <p class="card-text">price: Rs.400.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c7.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">THINK AND GROW RICH</h5>
                    <p class="card-text">price: Rs.200.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c8.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">THE GIRL ON THE TRAIN</h5>
                    <p class="card-text">price: Rs.300.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12" style="background-color: lightpink;">
                <p>Copyright © 2021 Book Publishing Company, Developed by kayalvizhi.</p>
            </div>
        </div>
    </div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

</body>

</html>

```
## OUTPUT:
![output](./static/img/output1.jpg)
![output](./static/img/output2.jpg)
![output](./static/img/output3.jpg)

## CODE VALIDATION REPORT:
![output](./static/img/report1.jpg)


## RESULT:
```
Thus a website is designed for the book publishing company and is hosted in the 
URL: http://kayalvizhi.student.saveetha.in:8000/responsivepage. HTML code is validated.