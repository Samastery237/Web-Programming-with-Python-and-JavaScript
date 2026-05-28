document.addEventListener('DOMContentLoaded', function() {
    const amountInput = document.getElementById('amount');
    const currencySelect = document.getElementById('currency-select');
    const convertBtn = document.getElementById('convert-btn');
    const resultDisplay = document.getElementById('result');

    convertBtn.addEventListener('click', async function() {
        const amount = parseFloat(amountInput.value);
        const selectedCurrency = currencySelect.value;

        if (isNaN(amount) || amount <= 0) {
            resultDisplay.textContent = 'Please enter a valid amount greater than 0.';
            return;
        }

        resultDisplay.textContent = 'Converting...';

        try {
            const response = await fetch('https://api.exchangerate-api.com/v4/latest/USD');
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            const rate = data.rates[selectedCurrency];

            if (rate) {
                const convertedAmount = (amount * rate).toFixed(2);
                resultDisplay.textContent = `${amount} USD is equal to ${convertedAmount} ${selectedCurrency}.`;
            } else {
                resultDisplay.textContent = 'Error: Selected currency rate not found.';
            }

        } catch (error) {
            console.error('Error fetching exchange rates:', error);
            resultDisplay.textContent = 'Failed to load exchange rates. Please check your connection.';
        }
    });
});