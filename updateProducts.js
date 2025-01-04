const fs = require('fs');
const path = require('path');

// File paths for your HTML files
const indexFilePath = path.join(__dirname, 'index.html');
const productFilePath = path.join(__dirname, 'Product', 'product.html');

// Function to add product details to the index.html
function addProductToIndex(homeView) {
    let pageContent = fs.readFileSync(indexFilePath, 'utf-8');
    const insertPosition = pageContent.indexOf('<div class="grid" id="product-grid">');

    if (insertPosition !== -1) {
        // Insert the product HTML after the grid div
        const updatedContent = 
            pageContent.slice(0, insertPosition + '<div class="grid" id="product-grid">'.length) +
            '\n' + homeView + 
            pageContent.slice(insertPosition + '<div class="grid" id="product-grid">'.length);

        fs.writeFileSync(indexFilePath, updatedContent, 'utf-8');
        console.log('Main HTML successfully updated!');
    } else {
        console.error('Failed to find insertion point in index.html');
    }
}

// Function to add product details to the product.html
function addProductToProductPage(productView) {
    let pageContent = fs.readFileSync(productFilePath, 'utf-8');
    const insertPosition = pageContent.indexOf('const productData = {');

    if (insertPosition !== -1) {
        // Insert the product object after the productData declaration
        const updatedContent = 
            pageContent.slice(0, insertPosition + 'const productData = {'.length) +
            '\n' + productView + 
            pageContent.slice(insertPosition + 'const productData = {'.length);

        fs.writeFileSync(productFilePath, updatedContent, 'utf-8');
        console.log('Product HTML successfully updated!');
    } else {
        console.error('Failed to find insertion point in product.html');
    }
}

// Simulated user input for home view and product view
const homeView = `
    <a href="Product/product.html?product=123" class="card">
        <img src="example.jpg" alt="Example Product">
        <div class="card-content">
            <h2>Example Product</h2>
            <p class="price">100DA</p>
            <p class="condition">Condition: New</p>
        </div>
    </a>
`;

const productView = `
    '123': {
        name: 'Example Product',
        price: '100DA',
        condition: 'New',
        description: 'This is an example product description.',
        images: ['example.jpg'],
        link: 'Product/product.html?product=123'
    },
`;

// Call the functions to update the HTML files
addProductToIndex(homeView);
addProductToProductPage(productView);
