import { useState, useEffect } from "react";
import ProductCard from "./ProductCard";

const BASE_URL = "http://localhost:8000/api/v1";

export default function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${BASE_URL}/products/`)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch products");
        return res.json();
      })
      .then((data) => setProducts(data))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p style={styles.center}>Loading products...</p>;
  if (error) return <p style={{ ...styles.center, color: "red" }}>{error}</p>;

  return (
    <div style={styles.page}>
      <h1 style={styles.title}>Products</h1>
      <div style={styles.grid}>
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

const styles = {
  page: { maxWidth: "1100px", margin: "0 auto", padding: "2rem", fontFamily: "sans-serif" },
  title: { fontSize: "2rem", marginBottom: "1.5rem", color: "#111" },
  grid: { display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))", gap: "1.5rem" },
  center: { textAlign: "center", marginTop: "4rem", fontSize: "1.1rem" },
};