import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class StockManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Management System")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")
        
        self.products = []
        self.total_sales = 0
        self.total_profit = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="📦 STOCK MANAGEMENT SYSTEM", 
                        font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#2c3e50")
        title.pack(pady=20)
        
        # Button Frame
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)
        
        buttons = [
            ("➕ Add Product", self.add_product, "#3498db"),
            ("📝 Update Product", self.update_product, "#f39c12"),
            ("🗑️ Delete Product", self.delete_product, "#e74c3c"),
            ("📥 Add Stock", self.add_stock, "#2ecc71"),
            ("📤 Remove Stock", self.remove_stock, "#e67e22"),
            ("💰 Sell Product", self.sell, "#9b59b6"),
            ("📊 View Stats", self.show_stats, "#1abc9c"),
        ]
        
        for i, (text, command, color) in enumerate(buttons):
            btn = tk.Button(btn_frame, text=text, command=command, 
                          width=18, height=2, font=("Arial", 10, "bold"),
                          bg=color, fg="white", cursor="hand2")
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
        
        # Products Table
        table_frame = tk.Frame(self.root, bg="#f0f0f0")
        table_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        tk.Label(table_frame, text="📋 Product List", font=("Arial", 14, "bold"),
                bg="#f0f0f0", fg="#2c3e50").pack(anchor="w", pady=(0, 10))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        self.tree = ttk.Treeview(table_frame, columns=("Name", "Cost", "Price", "Stock", "Value"),
                                show="headings", yscrollcommand=scrollbar.set, height=12)
        scrollbar.config(command=self.tree.yview)
        
        self.tree.heading("Name", text="Product Name")
        self.tree.heading("Cost", text="Cost Price")
        self.tree.heading("Price", text="Sell Price")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Value", text="Stock Value")
        
        self.tree.column("Name", width=200)
        self.tree.column("Cost", width=100)
        self.tree.column("Price", width=100)
        self.tree.column("Stock", width=100)
        self.tree.column("Value", width=150)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Stats Bar
        self.stats_label = tk.Label(self.root, text="", font=("Arial", 11),
                                   bg="#34495e", fg="white", pady=10)
        self.stats_label.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.update_display()
    
    def update_display(self):
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add products
        total_value = 0
        for i, p in enumerate(self.products):
            value = p["price"] * p["stock"]
            total_value += value
            self.tree.insert("", tk.END, values=(
                p["name"], 
                f"${p['cost']:.2f}", 
                f"${p['price']:.2f}", 
                p["stock"],
                f"${value:.2f}"
            ))
        
        # Update stats
        self.stats_label.config(text=f"💰 Total Sales: ${self.total_sales:.2f}  |  "
                                    f"📈 Net Profit: ${self.total_profit:.2f}  |  "
                                    f"📦 Stock Value: ${total_value:.2f}")
    
    def add_product(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Product")
        dialog.geometry("350x250")
        dialog.configure(bg="#ecf0f1")
        
        tk.Label(dialog, text="Product Name:", bg="#ecf0f1", font=("Arial", 10)).pack(pady=(20, 5))
        name_entry = tk.Entry(dialog, width=30, font=("Arial", 10))
        name_entry.pack()
        
        tk.Label(dialog, text="Cost Price:", bg="#ecf0f1", font=("Arial", 10)).pack(pady=(10, 5))
        cost_entry = tk.Entry(dialog, width=30, font=("Arial", 10))
        cost_entry.pack()
        
        tk.Label(dialog, text="Selling Price:", bg="#ecf0f1", font=("Arial", 10)).pack(pady=(10, 5))
        price_entry = tk.Entry(dialog, width=30, font=("Arial", 10))
        price_entry.pack()
        
        def save():
            try:
                name = name_entry.get().strip()
                cost = float(cost_entry.get())
                price = float(price_entry.get())
                
                if not name:
                    messagebox.showerror("Error", "Please enter a product name!")
                    return
                
                product = {"name": name, "cost": cost, "price": price, "stock": 0}
                self.products.append(product)
                self.update_display()
                messagebox.showinfo("Success", "✅ Product added successfully!")
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "❌ Please enter valid numbers for prices!")
        
        tk.Button(dialog, text="Save Product", command=save, bg="#27ae60", fg="white",
                 font=("Arial", 10, "bold"), cursor="hand2", pady=5).pack(pady=20)
    
    def update_product(self):
        if not self.products:
            messagebox.showwarning("Warning", "⚠️ No products available!")
            return
        
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "⚠️ Please select a product to update!")
            return
        
        index = self.tree.index(selected[0])
        product = self.products[index]
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Update Product")
        dialog.geometry("350x250")
        dialog.configure(bg="#ecf0f1")
        
        tk.Label(dialog, text="Product Name:", bg="#ecf0f1", font=("Arial", 10)).pack(pady=(20, 5))
        name_entry = tk.Entry(dialog, width=30, font=("Arial", 10))
        name_entry.insert(0, product["name"])
        name_entry.pack()
        
        tk.Label(dialog, text="Cost Price:", bg="#ecf0f1", font=("Arial", 10)).pack(pady=(10, 5))
        cost_entry = tk.Entry(dialog, width=30, font=("Arial", 10))
        cost_entry.insert(0, product["cost"])
        cost_entry.pack()
        
        tk.Label(dialog, text="Selling Price:", bg="#ecf0f1", font=("Arial", 10)).pack(pady=(10, 5))
        price_entry = tk.Entry(dialog, width=30, font=("Arial", 10))
        price_entry.insert(0, product["price"])
        price_entry.pack()
        
        def save():
            try:
                self.products[index]["name"] = name_entry.get().strip()
                self.products[index]["cost"] = float(cost_entry.get())
                self.products[index]["price"] = float(price_entry.get())
                self.update_display()
                messagebox.showinfo("Success", "✅ Product updated successfully!")
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "❌ Please enter valid numbers!")
        
        tk.Button(dialog, text="Update Product", command=save, bg="#f39c12", fg="white",
                 font=("Arial", 10, "bold"), cursor="hand2", pady=5).pack(pady=20)
    
    def delete_product(self):
        if not self.products:
            messagebox.showwarning("Warning", "⚠️ No products available!")
            return
        
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "⚠️ Please select a product to delete!")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this product?"):
            index = self.tree.index(selected[0])
            self.products.pop(index)
            self.update_display()
            messagebox.showinfo("Success", "✅ Product deleted successfully!")
    
    def add_stock(self):
        if not self.products:
            messagebox.showwarning("Warning", "⚠️ No products available!")
            return
        
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "⚠️ Please select a product!")
            return
        
        index = self.tree.index(selected[0])
        qty = simpledialog.askinteger("Add Stock", "Enter quantity to add:", minvalue=1)
        
        if qty:
            self.products[index]["stock"] += qty
            self.update_display()
            messagebox.showinfo("Success", f"✅ Added {qty} units to stock!")
    
    def remove_stock(self):
        if not self.products:
            messagebox.showwarning("Warning", "⚠️ No products available!")
            return
        
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "⚠️ Please select a product!")
            return
        
        index = self.tree.index(selected[0])
        qty = simpledialog.askinteger("Remove Stock", "Enter quantity to remove:", minvalue=1)
        
        if qty:
            if qty > self.products[index]["stock"]:
                messagebox.showerror("Error", "⚠️ Not enough stock!")
            else:
                self.products[index]["stock"] -= qty
                self.update_display()
                messagebox.showinfo("Success", f"✅ Removed {qty} units from stock!")
    
    def sell(self):
        if not self.products:
            messagebox.showwarning("Warning", "⚠️ No products available!")
            return
        
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "⚠️ Please select a product to sell!")
            return
        
        index = self.tree.index(selected[0])
        product = self.products[index]
        
        qty = simpledialog.askinteger("Sell Product", f"Enter quantity to sell (Available: {product['stock']}):", 
                                     minvalue=1)
        
        if qty:
            if qty > product["stock"]:
                messagebox.showerror("Error", "⚠️ Not enough stock!")
            else:
                sale_value = product["price"] * qty
                cost_value = product["cost"] * qty
                profit = sale_value - cost_value
                
                self.products[index]["stock"] -= qty
                self.total_sales += sale_value
                self.total_profit += profit
                
                self.update_display()
                messagebox.showinfo("Sale Successful!", 
                                   f"✅ Sale completed!\n\n"
                                   f"💰 Sale Amount: ${sale_value:.2f}\n"
                                   f"📈 Profit: ${profit:.2f}\n"
                                   f"📦 Remaining Stock: {product['stock']}")
    
    def show_stats(self):
        total_value = sum(p["price"] * p["stock"] for p in self.products)
        total_items = sum(p["stock"] for p in self.products)
        
        stats_text = (
            f"📊 BUSINESS STATISTICS\n\n"
            f"💰 Total Sales: ${self.total_sales:.2f}\n"
            f"📈 Net Profit: ${self.total_profit:.2f}\n"
            f"📦 Total Stock Value: ${total_value:.2f}\n"
            f"🔢 Total Items in Stock: {total_items}\n"
            f"📝 Number of Products: {len(self.products)}"
        )
        
        messagebox.showinfo("Business Statistics", stats_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagementSystem(root)
    root.mainloop()