// JavaScript code for client-side interactivity

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the transaction type select element
    document.getElementById('transaction_type').addEventListener('change', function() {
        var transactionType = this.value;
        var amountInput = document.getElementById('amount');

        // Update the placeholder text of the amount input based on the selected transaction type
        if (transactionType === 'income') {
            amountInput.placeholder = 'Income Amount';
        } else {
            amountInput.placeholder = 'Expense Amount';
        }
    });
});

