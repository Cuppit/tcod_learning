#!/usr/bin/env python3
import traceback

import tcod

import color
import exceptions
import input_handlers
import setup_game

def main() -> None: 
    screen_width = 80
    screen_height = 50

    
    tileset = tcod.tileset.load_tilesheet(
         "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
         #"buddy.png", 16, 16, tcod.tileset.CHARMAP_TCOD
        
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()
    
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        try:
            while True:
                print("DEBUG -- main.py, mian()",type(root_console))
                handler.on_render(console=root_console)
                context.present(root_console)
                
                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                    )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise
            
            # engine.event_handler.handle_events(context)
            
	
	
if __name__ == "__main__":
	main()