from nicegui import ui, app
from .models import Counter

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter in user storage (persists across sessions)
        if 'counter' not in app.storage.user:
            app.storage.user['counter'] = Counter().model_dump()
        
        counter_data = Counter(**app.storage.user['counter'])
        
        # Create UI elements
        with ui.column().classes('items-center gap-8 p-8'):
            ui.label('Simple Counter').classes('text-3xl font-bold text-center')
            
            # Counter display
            count_label = ui.label(str(counter_data.value)).classes('text-6xl font-mono text-center p-4 bg-gray-100 rounded-lg min-w-32').mark('count-display')
            
            # Buttons row
            with ui.row().classes('gap-4'):
                decrement_btn = ui.button('-', 
                    color='red'
                ).classes('text-2xl px-6 py-3').mark('decrement')
                
                increment_btn = ui.button('+', 
                    color='green'
                ).classes('text-2xl px-6 py-3').mark('increment')
        
        def increment():
            counter_data.value += 1
            app.storage.user['counter'] = counter_data.model_dump()
            count_label.set_text(str(counter_data.value))
            ui.notify(f'Counter incremented to {counter_data.value}', type='positive')
        
        def decrement():
            counter_data.value -= 1
            app.storage.user['counter'] = counter_data.model_dump()
            count_label.set_text(str(counter_data.value))
            ui.notify(f'Counter decremented to {counter_data.value}', type='info')
        
        increment_btn.on_click(increment)
        decrement_btn.on_click(decrement)