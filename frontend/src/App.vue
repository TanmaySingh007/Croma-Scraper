<template>
  <div class="header">
    <span>CROMA HEADER</span>
  </div>
  <div>
    <h1>Croma Televisions & Accessories - Product Cards</h1>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div class="product-grid">
        <div v-for="product in products" :key="product.product_id" class="product-card">
          <h3>{{ product.title }}</h3>
          <div class="prices">
            <span class="price" v-if="product.price">{{ product.price }}</span>
            <span class="sale-price" v-if="product.sale_price">{{ product.sale_price }}</span>
          </div>
          <div class="discount" v-if="product.discount_message">{{ product.discount_message }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      products: [],
      error: ''
    }
  },
  mounted() {
    fetch('http://localhost:5000/products')
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          this.products = data.products;
        } else {
          this.error = data.message || 'No products found';
        }
      })
      .catch(() => {
        this.error = 'Failed to fetch products';
      });
  }
}
</script>

<style>
.header {
  background-color: #000;
  padding: 20px;
  text-align: center;
  font-size: 24px;
  font-weight: bold;
}
.header span {
  color: #fff;
}
.error {
  color: red;
  margin: 20px 0;
}
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin: 32px 0;
}
.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.product-card h3 {
  margin: 0 0 12px 0;
  font-size: 18px;
}
.prices {
  margin-bottom: 8px;
}
.price {
  text-decoration: line-through;
  color: #888;
  margin-right: 8px;
}
.sale-price {
  color: #e53935;
  font-weight: bold;
}
.discount {
  color: #388e3c;
  font-size: 14px;
  margin-top: 4px;
}
</style>



