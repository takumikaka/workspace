//////////////////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2014-present, Egret Technology.
//  All rights reserved.
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are met:
//
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//     * Neither the name of the Egret nor the
//       names of its contributors may be used to endorse or promote products
//       derived from this software without specific prior written permission.
//
//  THIS SOFTWARE IS PROVIDED BY EGRET AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
//  OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
//  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
//  IN NO EVENT SHALL EGRET AND CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
//  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
//  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;LOSS OF USE, DATA,
//  OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
//  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////////////////


class Main extends egret.DisplayObjectContainer {

    public constructor() {
        super();
        this.once( egret.Event.ADDED_TO_STAGE, this.onAddToStage, this );
    }

    private onAddToStage( event:egret.Event ) {
        var imgLoader:egret.ImageLoader = new egret.ImageLoader;
        imgLoader.once( egret.Event.COMPLETE, this.imgLoadHandler, this );
        imgLoader.load("resource/cartoon-egret_00.png");
    }

    private _bird:egret.Bitmap;

    private imgLoadHandler( evt:egret.Event ):void {
        this._bird = new egret.Bitmap( evt.currentTarget.data );
        this.addChild( this._bird );

        this._bird.anchorOffsetX = this._bird.width / 2;
        this._bird.anchorOffsetY = this._bird.height / 2;
        this._bird.x = this.stage.stageWidth * 0.5;
        this._bird.y = this.stage.stageHeight * 0.618;
 
    }

}
