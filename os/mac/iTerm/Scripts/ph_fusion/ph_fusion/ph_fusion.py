#!/usr/bin/env python3.7

import iterm2
# This script was created with the "basic" environment which does not support adding dependencies


async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window

    if window is not None:
        await window.async_set_fullscreen(True)

        # Split the tab into panes
        bottom_left = app.current_terminal_window.current_tab.current_session
        bottom_right = await bottom_left.async_split_pane(vertical=True)
        top_left = await bottom_left.async_split_pane(vertical=False, before=True)
        top_right = await bottom_right.async_split_pane(vertical=False, before=True)

        # Run commands
        await top_left.async_send_text('rz \n')
        await top_left.async_send_text('fs \n')

        await top_right.async_send_text('rz \n')
        await top_right.async_send_text('nrd \n')

        await bottom_left.async_send_text('rz \n')
        await bottom_left.async_send_text('nrt \n')

        await bottom_right.async_send_text('rz \n')

    else:
        print("No current window")

iterm2.run_until_complete(main)
