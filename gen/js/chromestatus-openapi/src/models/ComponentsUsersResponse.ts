/* tslint:disable */
/* eslint-disable */
/**
 * chomestatus API
 * The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
import type { ComponentsUser } from './ComponentsUser';
import {
    ComponentsUserFromJSON,
    ComponentsUserFromJSONTyped,
    ComponentsUserToJSON,
} from './ComponentsUser';
import type { OwnersAndSubscribersOfComponent } from './OwnersAndSubscribersOfComponent';
import {
    OwnersAndSubscribersOfComponentFromJSON,
    OwnersAndSubscribersOfComponentFromJSONTyped,
    OwnersAndSubscribersOfComponentToJSON,
} from './OwnersAndSubscribersOfComponent';

/**
 * 
 * @export
 * @interface ComponentsUsersResponse
 */
export interface ComponentsUsersResponse {
    /**
     * 
     * @type {Array<ComponentsUser>}
     * @memberof ComponentsUsersResponse
     */
    users?: Array<ComponentsUser>;
    /**
     * 
     * @type {Array<OwnersAndSubscribersOfComponent>}
     * @memberof ComponentsUsersResponse
     */
    components?: Array<OwnersAndSubscribersOfComponent>;
}

/**
 * Check if a given object implements the ComponentsUsersResponse interface.
 */
export function instanceOfComponentsUsersResponse(value: object): value is ComponentsUsersResponse {
    return true;
}

export function ComponentsUsersResponseFromJSON(json: any): ComponentsUsersResponse {
    return ComponentsUsersResponseFromJSONTyped(json, false);
}

export function ComponentsUsersResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): ComponentsUsersResponse {
    if (json == null) {
        return json;
    }
    return {
        
        'users': json['users'] == null ? undefined : ((json['users'] as Array<any>).map(ComponentsUserFromJSON)),
        'components': json['components'] == null ? undefined : ((json['components'] as Array<any>).map(OwnersAndSubscribersOfComponentFromJSON)),
    };
}

export function ComponentsUsersResponseToJSON(value?: ComponentsUsersResponse | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'users': value['users'] == null ? undefined : ((value['users'] as Array<any>).map(ComponentsUserToJSON)),
        'components': value['components'] == null ? undefined : ((value['components'] as Array<any>).map(OwnersAndSubscribersOfComponentToJSON)),
    };
}

