from nicegui import ui, app

def create():
    @ui.page('/')
    def page():
        ui.label('Simple Counter').classes('text-h4 q-mb-md')
        
        # Initialize counter value in user storage to persist across sessions
        if 'counter' not in app.storage.user:
            app.storage.user['counter'] = 0
        
        # Create the counter display
        counter_label = ui.label().classes('text-h2 q-mb-md')
        
        def update_display():
            counter_label.set_text(f'Count: {app.storage.user["counter"]}')
        
        def increment():
            app.storage.user['counter'] += 1
            update_display()
            ui.notify(f'Incremented to {app.storage.user["counter"]}', type='positive')
        
        def decrement():
            app.storage.user['counter'] -= 1
            update_display()
            ui.notify(f'Decremented to {app.storage.user["counter"]}', type='info')
        
        def reset():
            app.storage.user['counter'] = 0
            update_display()
            ui.notify('Counter reset to 0', type='warning')
        
        # Initial display update
        update_display()
        
        # Create buttons
        with ui.row().classes('q-gutter-md'):
            ui.button('Increment (+1)', on_click=increment, color='positive').classes('q-px-lg')
            ui.button('Decrement (-1)', on_click=decrement, color='negative').classes('q-px-lg')
            ui.button('Reset', on_click=reset, color='warning').classes('q-px-lg')