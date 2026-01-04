console.log("script.js loaded");

fetch("/products")
  .then(response => response.json())
  .then(products => {
    console.log("Products:", products);

    const container = document.getElementById("products");

    products.forEach(product => {
      const card = document.createElement("div");
      card.className = "product-card";

      card.innerHTML = `
        <img src="/static/images/${product.image}" />
        <h3>${product.name}</h3>
        <p>₹${product.price}</p>
        <button>Add to Cart</button>
      `;

      container.appendChild(card);
    });
  })
  .catch(err => console.error("Error:", err));


