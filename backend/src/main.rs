mod commands;
mod models;
mod utils;

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::model::load_model,
            commands::file_io::read_file,
            commands::system::get_system_info,
        ])
        .run(tauri::generate_context!())
        .expect("error while running Tauri application");
}
