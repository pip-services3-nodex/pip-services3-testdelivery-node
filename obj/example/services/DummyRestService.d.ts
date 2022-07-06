import { IReferences } from 'pip-services3-commons-nodex';
import { ConfigParams } from 'pip-services3-commons-nodex';
import { RestService } from 'pip-services3-rpc-nodex';
export declare class DummyRestService extends RestService {
    private _controller;
    constructor();
    configure(config: ConfigParams): void;
    setReferences(references: IReferences): void;
    private getPageByFilter;
    private getOneById;
    private create;
    private update;
    private deleteById;
    register(): void;
}
