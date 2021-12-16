use bevy::prelude::*;

#[derive(Default)]
pub struct FounderyPlugin;

impl Plugin for FounderyPlugin {
    fn build(&self, app: &mut AppBuilder) {
        app.init_asset_loader::<FounderyPlugin>();
    }
}
