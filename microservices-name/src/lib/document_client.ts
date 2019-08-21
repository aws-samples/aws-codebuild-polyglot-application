import { DocumentClient } from 'aws-sdk/clients/dynamodb';
import { AWSError } from 'aws-sdk/lib/error';
import { Request } from 'aws-sdk/lib/request';
var AWS = require('aws-sdk/global');

/**
 * Document Client Interface
 * 
 * A replaceable document client object that can be replaced 
 */
export interface DocumentClientInterface {
  query(params: DocumentClient.QueryInput, callback?: (err: AWSError, data: DocumentClient.QueryOutput) => void): Request<DocumentClient.QueryOutput, AWSError>;

  scan(params: DocumentClient.ScanInput, callback?: (err: AWSError, data: DocumentClient.ScanOutput) => void): Request<DocumentClient.ScanOutput, AWSError>;
}

/**
 * Default Document Client
 * 
 * @type DocumentClientInterface
 */
export let DefaultDocumentClient: DocumentClientInterface = new DocumentClient({ endpoint: process.env.AWS_SAM_LOCAL ? 'http://dynamodb:8000' : undefined });
export type QueryInput = DocumentClient.QueryInput
export type ScanInput = DocumentClient.ScanInput
export type ItemList = DocumentClient.ItemList