"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.DummyCommandableHttpService = void 0;
const pip_services3_commons_nodex_1 = require("pip-services3-commons-nodex");
const pip_services3_rpc_nodex_1 = require("pip-services3-rpc-nodex");
class DummyCommandableHttpService extends pip_services3_rpc_nodex_1.CommandableHttpService {
    constructor() {
        super('dummies2');
        this._dependencyResolver.put('controller', new pip_services3_commons_nodex_1.Descriptor('pip-services-dummies', 'controller', 'default', '*', '*'));
    }
    register() {
        // if (!this._swaggerAuto && this._swaggerEnabled) {
        //     this.registerOpenApiSpec("swagger yaml content");
        // }
        super.register();
    }
}
exports.DummyCommandableHttpService = DummyCommandableHttpService;
//# sourceMappingURL=DummyCommandableHttpService.js.map