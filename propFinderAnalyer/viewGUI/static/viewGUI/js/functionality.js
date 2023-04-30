 // This is the JS for the various components in the data_display.html page
 // It initiates a map, modal, and calculates a cash on cash return and more

 function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {

        zoom: 10,
        center: {lat: 41.9198, lng: -88.0817} //glendale heights center
    });


    var markers = [];

    // Loop over all the rows in the table
    var rows = document.querySelectorAll('.table-row');
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];

        // Create a marker for this row's location
        var lat = row.getAttribute('data-lat');
        var lng = row.getAttribute('data-lon');
        var marker = new google.maps.Marker({
            position: {lat: parseFloat(lat), lng: parseFloat(lng)},
            map: map
        });
        markers.push(marker);

        // Add event listeners to the row
        row.addEventListener('mouseover', function() {
            var index = Array.from(rows).indexOf(this);
            markers[index].setAnimation(google.maps.Animation.BOUNCE);
        });

        row.addEventListener('mouseout', function() {
            var index = Array.from(rows).indexOf(this);
            markers[index].setAnimation(null);
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems);
});


// event listeer for submit in modal
// reference to the Submit button
const submitBtn = document.getElementById('submit-btn');

// Add an event listener that executes a function when clicked
submitBtn.addEventListener('click', function() {
    // Call your function here
    calculateCashOnCash();
});


//    cash on cash calc
function calculateCashOnCash() {

  // Get the input values from the form
  var monthlyRentalIncome = Number(document.getElementById("monthly rental income").value);
  var tax = Number(document.getElementById("tax").value);
  var insurance = Number(document.getElementById("insurance").value);

  var utilities = Number(document.getElementById("utilities").value);
  var HOA = Number(document.getElementById("HOA").value);

  var repairs = Number(document.getElementById("repairs").value);

//      ENTER  'cash' for cash or nothing to skip funct
  var downPayment = document.getElementById("downPayment").value;
//     add nothing to skip
  var interestRate = Number(document.getElementById("interestRate").value);
  var loanTerm = Number(document.getElementById("loan Term").value);
  var closingCosts = Number(document.getElementById("closingCosts").value);

  // Loop over the table rows and add a new column with the result
  var rows = document.querySelectorAll('.table-row');
  for (var i = 0; i < rows.length; i++) {
    var row = rows[i];
    var price = parseFloat(row.querySelector('td:nth-child(5)').innerText);
    var cashOnCashCell = document.createElement('td');

     //if cash
    if (downPayment === 'cash') {
        // code to be executed if downPayment is equal to 'cash'
        //other calc
        var monthlyExp = tax + insurance + utilities + HOA + repairs;
        //cash flow
        var cashFlow = monthlyRentalIncome - monthlyExp;
        var yearlyCashFlow = cashFlow * 12;

        //do cashflow / price for %
        var cashOnCash = (yearlyCashFlow / (price + closingCosts)) * 100;

    } else {

        //calc the monthly mrotage NEED PRICE TO DO IT
        var monthlyInterestRate = interestRate / 1200; // Convert annual interest rate to monthly rate
        var totalPayments = loanTerm * 12; // Convert loan term from years to months
        var denominator = Math.pow(1 + monthlyInterestRate, -totalPayments);
        var loanAmount = price - Number(downPayment);
        var monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - denominator);

        //monthly expenses added maybe mortgage if getting
        var monthlyExp = tax + insurance + utilities + HOA + repairs + monthlyPayment;
        var cashFlow = monthlyRentalIncome - monthlyExp;
        var yearlyCashFlow = cashFlow * 12;
        var cashOnCash = (yearlyCashFlow / (Number(downPayment) + closingCosts)) * 100;
    } //end else

        // new code
        var cashOnCashCell = row.querySelector('td:nth-child(11)');
        cashOnCashCell.innerText = cashOnCash.toFixed(2) + '%';
  }  //for loop

} //coc funct



