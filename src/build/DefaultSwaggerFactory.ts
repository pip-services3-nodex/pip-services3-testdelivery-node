/** @module build */
import { Factory } from 'pip-services3-components-nodex';
import { Descriptor } from 'pip-services3-commons-nodex';

import { SwaggerService } from '../services/SwaggerService';

/**
 * Creates Swagger components by their descriptors.
 * 
 * @see [[https://pip-services3-nodex.github.io/pip-services3-components-nodex/classes/build.factory.html Factory]]
 * @see [[HttpEndpoint]]
 * @see [[HeartbeatRestService]]
 * @see [[StatusRestService]] 
 */
export class DefaultSwaggerFactory extends Factory {
    private static readonly SwaggerServiceDescriptor: Descriptor = new Descriptor("pip-services", "swagger-service", "*", "*", "1.0");

    /**
	 * Create a new instance of the factory.
	 */
    public constructor() {
        super();
        this.registerAsType(DefaultSwaggerFactory.SwaggerServiceDescriptor, SwaggerService);
    }
}
