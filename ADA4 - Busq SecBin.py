import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import pprint # Para imprimir diccionarios bonitos

class ModernSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmos de Búsqueda Detallados - Axel Dev")
        self.root.geometry("1100x750") # Un poco más ancho para ver los logs
        self.root.configure(bg="#1e1e1e")

        # Variables de estado
        self.data_list = []
        self.is_sorted = False
        
        # Estilos
        self.setup_styles()
        
        # Interfaz
        self.create_header()
        self.create_body()

        # Datos iniciales
        self.generate_data()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 18, "bold"), foreground="#00adb5")
        style.configure("TButton", font=("Segoe UI", 9, "bold"), background="#393e46", foreground="#eeeeee", borderwidth=0)
        style.map("TButton", background=[("active", "#00adb5")])

    def create_header(self):
        header_frame = ttk.Frame(self.root, padding="20")
        header_frame.pack(fill="x")
        ttk.Label(header_frame, text="Tipos de Búsqueda", style="Header.TLabel").pack(side="left")
        
        btn_frame = ttk.Frame(header_frame)
        btn_frame.pack(side="right")
        ttk.Button(btn_frame, text="Ordenar Lista (A-Z)", command=self.sort_data).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Regenerar Random", command=self.generate_data).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Limpiar Log", command=self.clear_log).pack(side="left", padx=5)
        tk.Frame(self.root, bg="#393e46", height=2).pack(fill="x", padx=20)

    def create_body(self):
        top_frame = ttk.Frame(self.root, padding="20")
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Valores Generados (Array):").pack(anchor="w", pady=(0, 5))
        self.txt_display = tk.Text(top_frame, height=3, bg="#2b2b2b", fg="#00adb5", font=("Consolas", 10), bd=0, padx=10, pady=10)
        self.txt_display.pack(fill="x", pady=(0, 15))
        self.txt_display.config(state="disabled")

        control_frame = ttk.Frame(top_frame)
        control_frame.pack(fill="x")
        
        ttk.Label(control_frame, text="Método:").pack(side="left", padx=(0, 5))
        self.combo_method = ttk.Combobox(control_frame, values=["Secuencial", "Binaria", "Hash (Diccionario)"], state="readonly", width=20)
        self.combo_method.current(0)
        self.combo_method.pack(side="left", padx=(0, 15))

        ttk.Label(control_frame, text="Buscar Valor:").pack(side="left", padx=(0, 5))
        self.entry_search = ttk.Entry(control_frame, width=15)
        self.entry_search.pack(side="left", padx=(0, 15))
        ttk.Button(control_frame, text="Ejecutar Trace", command=self.start_search).pack(side="left")

        bottom_frame = ttk.Frame(self.root, padding="20")
        bottom_frame.pack(fill="both", expand=True)
        ttk.Label(bottom_frame, text="Bitácora de Ejecución (Paso a Paso):").pack(anchor="w", pady=(0, 5))

        self.log_text = tk.Text(bottom_frame, bg="#222831", fg="#eeeeee", font=("Consolas", 9), bd=0, padx=10, pady=10)
        self.log_text.pack(fill="both", expand=True)
        
        # Tags de colores
        self.log_text.tag_config("highlight", foreground="#f9ed69") # Amarillo
        self.log_text.tag_config("success", foreground="#00adb5")   # Cyan
        self.log_text.tag_config("error", foreground="#ff2e63")     # Rojo
        self.log_text.tag_config("process", foreground="#a8d8ea")   # Azul claro
        self.log_text.tag_config("subtle", foreground="#555555")    # Gris oscuro

    def generate_data(self):
        self.data_list = [random.randint(1, 500) for _ in range(100)]
        self.is_sorted = False
        self.update_display()
        self.log_step(">>> Nueva lista generada.", "subtle")

    def sort_data(self):
        self.data_list.sort()
        self.is_sorted = True
        self.update_display()
        self.log_step(">>> Lista ordenada.", "subtle")

    def update_display(self):
        self.txt_display.config(state="normal")
        self.txt_display.delete("1.0", tk.END)
        self.txt_display.insert("1.0", str(self.data_list))
        self.txt_display.config(state="disabled")

    def clear_log(self):
        self.log_text.delete("1.0", tk.END)

    def log_step(self, message, tag=None):
        self.log_text.insert(tk.END, message + "\n", tag)
        self.log_text.see(tk.END)

    def start_search(self):
        val_str = self.entry_search.get()
        if not val_str.isdigit():
            messagebox.showerror("Error", "Ingresa un número válido.")
            return

        target = int(val_str)
        method = self.combo_method.get()

        self.log_step("=" * 80, "subtle")
        self.log_step(f"INICIO: Búsqueda {method.upper()} | Objetivo: {target}", "highlight")
        
        start_time = time.perf_counter()
        
        if method == "Secuencial":
            self.search_sequential(target)
        elif method == "Binaria":
            self.search_binary(target)
        elif method == "Hash (Diccionario)":
            self.search_hash(target)
            
        end_time = time.perf_counter()
        elapsed = (end_time - start_time) * 1000
        self.log_step("-" * 80, "subtle")
        self.log_step(f"RESUMEN FINAL: Tiempo de ejecución total: {elapsed:.4f} ms", "highlight")
        self.log_step("=" * 80, "subtle")

    # --- ALGORITMOS DETALLADOS ---

    def search_sequential(self, target):
        """Muestra cada iteración sin resumir"""
        found = False
        self.log_step(f"Comenzando recorrido desde índice 0 hasta {len(self.data_list)-1}...", "process")
        
        for index, value in enumerate(self.data_list):
            # Imprimimos CADA paso
            match_symbol = "==" if value == target else "!="
            result_txt = "MATCH" if value == target else "..."
            tag = "success" if value == target else None
            
            self.log_step(f"Iteración {index}: ¿Array[{index}] ({value}) {match_symbol} {target}? -> {result_txt}", tag)

            if value == target:
                self.log_step(f"¡ÉXITO! Valor encontrado en posición {index}.", "success")
                found = True
                break # Quitamos esto si quieres buscar TODOS los duplicados, pero por def es first-match
        
        if not found:
            self.log_step(f"Recorrido terminado. El valor {target} NO existe en la lista.", "error")

    def search_binary(self, target):
        """Muestra los punteros Low, High, Mid en cada vuelta"""
        if not self.is_sorted:
            self.log_step("ERROR CRÍTICO: Lista no ordenada. Búsqueda abortada.", "error")
            return

        left = 0
        right = len(self.data_list) - 1
        found = False
        step = 1

        self.log_step(f"Rango inicial: [0 - {right}]", "process")

        while left <= right:
            mid = (left + right) // 2
            mid_val = self.data_list[mid]
            
            # Visualización detallada de los punteros
            self.log_step(f"\n--- Vuelta {step} ---", "process")
            self.log_step(f"  Punteros: Izq({left}) | Der({right}) -> Centro Calculado({mid})")
            self.log_step(f"  Comparación: ¿ValorCentro ({mid_val}) == Objetivo ({target})?")

            if mid_val == target:
                self.log_step(f"  RESULTADO: ¡Iguales! Encontrado en índice {mid}.", "success")
                found = True
                break
            elif mid_val < target:
                self.log_step(f"  DECISIÓN: {mid_val} < {target}. El objetivo es mayor.", "error")
                self.log_step(f"  ACCIÓN: Ignorar mitad izquierda. Nuevo Izq = {mid + 1}")
                left = mid + 1
            else:
                self.log_step(f"  DECISIÓN: {mid_val} > {target}. El objetivo es menor.", "error")
                self.log_step(f"  ACCIÓN: Ignorar mitad derecha. Nuevo Der = {mid - 1}")
                right = mid - 1
            step += 1
        
        if not found:
            self.log_step("\nEl puntero Izq cruzó al Der. El valor no existe.", "error")

    def search_hash(self, target):
        """Muestra la construcción de la tabla y luego la búsqueda"""
        hash_table = {}
        
        self.log_step("FASE 1: CONSTRUCCIÓN DE LA TABLA HASH (Indexación)", "highlight")
        self.log_step("Leyendo lista y asignando claves...", "process")
        
        # Simulación visual de llenado
        for index, value in enumerate(self.data_list):
            msg = f"  Leyendo Index[{index}] Val({value}) -> "
            
            if value in hash_table:
                msg += f"¡Colisión! Agregando índice a la lista de la clave {value}."
                hash_table[value].append(index)
            else:
                msg += f"Nueva Clave {value} creada. Asignando índice."
                hash_table[value] = [index]
            
            # Solo imprimimos detalles de los primeros 10 y últimos 5 para no colgar la UI si es muy rápido,
            # PERO como pediste detalle, lo imprimimos todo.
            self.log_step(msg)

        self.log_step("\n--- ESTADO FINAL DE LA TABLA HASH ---", "process")
        # Imprimir una versión legible de la tabla
        pretty_table = pprint.pformat(hash_table, compact=True)
        self.log_step(pretty_table, "subtle")
        self.log_step("-" * 40)

        self.log_step("FASE 2: BÚSQUEDA (Lookup O(1))", "highlight")
        self.log_step(f"Calculando Hash para objetivo {target}...", "process")
        
        if target in hash_table:
            indices = hash_table[target]
            self.log_step(f"  Key '{target}' existe en la tabla.", "success")
            self.log_step(f"  Value recuperado (Índices): {indices}", "success")
        else:
            self.log_step(f"  Key '{target}' NO encontrada en las claves de la tabla.", "error")
            self.log_step("  Retorno: None", "error")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernSearchApp(root)
    root.mainloop()