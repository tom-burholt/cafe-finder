import router from '../router';
import store from '../stores/store';

/**
 * plugins/index.ts
 *
 * Automatically included in `./src/main.ts`
 */

// Types

// Plugins
import vuetify from './vuetify'

export function registerPlugins (app) {
    app.use(vuetify);
    app.use(store);
    app.use(router);
}