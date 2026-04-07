export default function ProductCard({ product }) {
  return (
    <div style={styles.card}>
      <h2 style={styles.name}>{product.name}</h2>
      <p style={styles.description}>{product.description}</p>
      <p style={styles.price}>${product.price.toFixed(2)}</p>
    </div>
  );
}

const styles = {
  card: {
    border: "1px solid #e5e7eb", borderRadius: "12px", padding: "1.25rem",
    background: "#fff", boxShadow: "0 1px 4px rgba(0,0,0,0.06)",
    display: "flex", flexDirection: "column", gap: "0.5rem",
  },
  header: { display: "flex", justifyContent: "space-between", alignItems: "center" },
  category: { fontSize: "0.75rem", color: "#6b7280", textTransform: "uppercase", letterSpacing: "0.05em" },
  badge: { fontSize: "0.75rem", padding: "2px 8px", borderRadius: "999px", fontWeight: 600 },
  name: { fontSize: "1.1rem", fontWeight: 700, color: "#111", margin: 0 },
  description: { fontSize: "0.9rem", color: "#6b7280", margin: 0 },
  price: { fontSize: "1.25rem", fontWeight: 700, color: "#2563eb", margin: 0, marginTop: "auto" },
};