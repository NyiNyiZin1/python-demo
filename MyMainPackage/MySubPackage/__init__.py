<!-- /.modal-->
          <div class="modal fade" id="tenant-edit-confirm-modal"
            data-keyboard="false" data-backdrop="static" tabindex="-1"
            role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-primary" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h4 class="modal-title">テナント編集</h4>
                </div>
                <div class="modal-body">
                  <div id="tenant-edit-confirm-body" style="display: none;">
                    <p>下記の内容で保存しますか？</p>
                    <div class="row">
                      <label class="col-md-3 col-form-label"> <strong>テナント名</strong>
                      </label>
                      <div class="col-md-9">
                        <p class="form-control-static form-control-lg"
                          id="confirmEditTenantId" style="display: none"></p>
                        <p class="form-control-static form-control-lg"
                          id="confirmEditTenantName" style="height: auto; word-break: break-all;"></p>
                      </div>
                    </div>
                    <div class="row">
                      <label class="col-md-3 col-form-label"> <strong>種別</strong>
                      </label>
                      <div class="col-md-9">
                        <p class="form-control-static form-control-lg"
                          id="confirmEditTenantType" style="height: auto; word-break: break-all;"></p>
                      </div>
                    </div>
                    <div class="row">
                      <label class="col-md-3 col-form-label"> <strong>ドメインID</strong>
                      </label>
                      <div class="col-md-9">
                        <p class="form-control-static form-control-lg"
                          id="confirmEditDomainId" style="height: auto; word-break: break-all;"></p>
                      </div>
                    </div>
                    <div class="row">
                      <label class="col-md-3 col-form-label"> <strong>チャネルID</strong>
                      </label>
                      <div class="col-md-9">
                        <p class="form-control-static form-control-lg"
                          id="confirmEditChannelId" style="height: auto; word-break: break-all;"></p>
                      </div>
                    </div>
                    <div class="row">
                      <label class="col-md-3 col-form-label"> <strong>テナントログインID</strong>
                      </label>
                      <div class="col-md-9">
                        <p class="form-control-static form-control-lg"
                          id="confirmEditTenantLoginId"></p>
                      </div>
                    </div>
                    <div class="row">
                      <label class="col-md-3 col-form-label"> <strong>備考</strong>
                      </label>
                      <div class="col-md-9">
                        <p class="form-control-static form-control-lg"
                          id="confirmEditDescription" style="height: auto; word-break: break-all;"></p>
                      </div>
                    </div>
                  </div>

                  <div id="tenant-edit-done-body" style="display: none;">
                    <p id="editResult"></p>
                  </div>
                </div>
                <div class="modal-footer">
                  <button id="tenant-edit-cancel-btn" class="btn btn-secondary"
                    type="button" data-dismiss="modal">キャンセル1</button>
                  <button id="tenant-edit-btn" class="btn btn-primary"
                    type="button" data-toggle="modal" onclick="addQuestionModal()">保存</button>
                  <button id="tenant-edit-close-btn" class="btn btn-secondary"
                    type="button" data-dismiss="modal" style="display: none;">閉じる</button>
                </div>
              </div>
              <!-- /.modal-content-->
            </div>
            <!-- /.modal-dialog-->
          </div>
          <!-- /.modal-->