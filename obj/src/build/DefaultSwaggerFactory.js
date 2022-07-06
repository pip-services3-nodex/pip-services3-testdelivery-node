"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DefaultSwaggerFactory = void 0;
/** @module build */
const pip_services3_components_nodex_1 = require("pip-services3-components-nodex");
const pip_services3_commons_nodex_1 = require("pip-services3-commons-nodex");
const SwaggerService_1 = require("../services/SwaggerService");
/**
 * Creates Swagger components by their descriptors.
 *
 * @see [[https://pip-services3-nodex.github.io/pip-services3-components-nodex/classes/build.factory.html Factory]]
 * @see [[HttpEndpoint]]
 * @see [[HeartbeatRestService]]
 * @see [[StatusRestService]]
 */
class DefaultSwaggerFactory extends pip_services3_components_nodex_1.Factory {
    /**
     * Create a new instance of the factory.
     */
    constructor() {
        super();
        this.registerAsType(DefaultSwaggerFactory.SwaggerServiceDescriptor, SwaggerService_1.SwaggerService);
    }
}
exports.DefaultSwaggerFactory = DefaultSwaggerFactory;
DefaultSwaggerFactory.SwaggerServiceDescriptor = new pip_services3_commons_nodex_1.Descriptor("pip-services", "swagger-service", "*", "*", "1.0");
//# sourceMappingURL=DefaultSwaggerFactory.js.map