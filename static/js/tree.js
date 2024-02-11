/*
 * Fuel UX Tree
 * https://github.com/ExactTarget/fuelux
 *
 * Copyright (c) 2012 ExactTarget
 * Licensed under the MIT license.
 */

(function($, undefined) {

	var old = $.fn.tree;

	// TREE CONSTRUCTOR AND PROTOTYPE

	var Tree = function (element, options) {
		this.$element = $(element);
		this.options = $.extend({}, $.fn.tree.defaults, options);

		this.$element.on('click', '.tree-item i', $.proxy( function(ev) { this.selectItem(ev.currentTarget); } ,this));
		this.$element.on('click', '.tree-folder-header i', $.proxy( function(ev) { this.selectFolder($(ev.currentTarget).parent()); }, this));

		this.render();
	};

	Tree.prototype = {
		constructor: Tree,

		render: function () {
			this.populate(this.$element);
		},

		populate: function ($el, _items) {
			var self = this;
			var $parent = $el.parent();
			var loader = $parent.find('.tree-loader:eq(0)');

			loader.show();
            var callback = function (items) {
				loader.hide();

				$.each( items.data, function(index, value) {
					var $entity;
                    var count_label = '';
                    if (value.product_count != null) {
                        if (value.product_count == 0 && !self.$element.data('show-all')) return;
                        count_label = '<span class="badge">' + value.product_count + '</span>'
                    }
					if(value.type === "folder") {
						$entity = self.$element.find('.tree-folder:eq(0)').clone().show();
						$entity.find('.tree-folder-name').html(value.name + count_label).attr('href', value.href);
						$entity.find('.tree-loader').html(self.options.loadingHTML);
						$entity.find('.tree-folder-header').data(value);
					} else if (value.type === "item") {
						$entity = self.$element.find('.tree-item:eq(0)').clone().show();
						$entity.find('.tree-item-name').html(value.name + count_label).attr('href', value.href);
						$entity.data(value);
					}

					// Decorate $entity with data making the element
					// easily accessable with libraries like jQuery.
					//
					// Values are contained within the object returned
					// for folders and items as dataAttributes:
					//
					// {
					//     name: "An Item",
					//     type: 'item',
					//     dataAttributes = {
					//         'classes': 'required-item red-text',
					//         'data-parent': parentId,
					//         'guid': guid
					//     }
					// };

					var dataAttributes = value.dataAttributes || [];
					$.each(dataAttributes, function(key, value) {
						switch (key) {
						case 'class':
						case 'classes':
						case 'className':
							$entity.addClass(value);
							break;

						// id, style, data-*
						default:
							$entity.attr(key, value);
							break;
						}
					});

					if($el.hasClass('tree-folder-header')) {
						$parent.find('.tree-folder-content:eq(0)').append($entity);
					} else {
						$el.append($entity);
					}

                    if ('data' in value) {
                        var header = $entity.find('.tree-folder-header');
                        self.populate(header, value);

                        $entity.find('.' + self.options.closeIcon).eq(0)
                            .removeClass(self.options.closeIcon + ' ' + self.options.openIcon)
                            .addClass(self.options.openIcon);
                    }
				});

				// return newly populated folder
				self.$element.trigger('loaded', $parent);
			};

            if (_items == undefined) {
			    this.options.dataSource.data($el.data(), callback);
            } else {
                callback(_items);
            }
		},

		selectItem: function (el) {
			var $el = $(el);
			var $all = this.$element.find('.tree-selected');
			var data = [];

			if (this.options.multiSelect) {
				$.each($all, function(index, value) {
					var $val = $(value);
					if($val[0] !== $el[0]) {
						data.push( $(value).data() );
					}
				});
			} else if ($all[0] !== $el[0]) {
				$all.removeClass('tree-selected')
					.find('i').removeClass(this.options.selectedIcon).addClass(this.options.unselectedIcon);
				data.push($el.data());
			}

			var eventType = 'selected';
			if($el.hasClass('tree-selected')) {
				eventType = 'unselected';
				$el.removeClass('tree-selected');
				$el.find('i').removeClass(this.options.selectedIcon).addClass(this.options.unselectedIcon);
			} else {
				$el.addClass ('tree-selected');
				$el.find('i').removeClass(this.options.unselectedIcon).addClass(this.options.selectedIcon);
				if (this.options.multiSelect) {
					data.push( $el.data() );
				}
			}

			if(data.length) {
				this.$element.trigger('selected', {info: data});
			}

			// Return new list of selected items, the item
			// clicked, and the type of event:
			$el.trigger('updated', {
				info: data,
				item: $el,
				eventType: eventType
			});
		},

		selectFolder: function (el) {
			var $el = $(el);
			var $parent = $el.parent();
			var $treeFolderContent = $parent.find('.tree-folder-content');
			var $treeFolderContentFirstChild = $treeFolderContent.eq(0);

			var eventType, classToTarget, classToAdd;
			if ($el.find('.' + this.options.closeIcon).length) {
				eventType = 'opened';
				classToTarget = this.options.closeIcon;
				classToAdd = this.options.openIcon;

				$treeFolderContentFirstChild.show();
				if (!$treeFolderContent.children().length) {
					this.populate($el);
				}
			} else {
				eventType = 'closed';
				classToTarget = this.options.openIcon;
				classToAdd = this.options.closeIcon;

				$treeFolderContentFirstChild.hide();
				if (!this.options.cacheItems) {
					$treeFolderContentFirstChild.empty();
				}
			}

			$parent.find('.' + classToTarget).eq(0)
				.removeClass(this.options.closeIcon + ' ' + this.options.openIcon)
				.addClass(classToAdd);

			this.$element.trigger(eventType, $el.data());
		},

		selectedItems: function () {
			var $sel = this.$element.find('.tree-selected');
			var data = [];

			$.each($sel, function (index, value) {
				data.push($(value).data());
			});
			return data;
		},

		// collapses open folders
		collapse: function () {
			var cacheItems = this.options.cacheItems;

			// find open folders
			this.$element.find('.' + this.options.openIcon).each(function () {
				// update icon class
				var $this = $(this)
					.removeClass(this.options.closeIcon + ' ' + this.options.openIcon)
					.addClass(this.options.closeIcon);

				// "close" or empty folder contents
				var $parent = $this.parent().parent();
				var $folder = $parent.children('.tree-folder-content');

				$folder.hide();
				if (!cacheItems) {
					$folder.empty();
				}
			});
		}
	};


	// TREE PLUGIN DEFINITION

	$.fn.tree = function (option) {
		var args = Array.prototype.slice.call( arguments, 1 );
		var methodReturn;

		var $set = this.each(function () {
			var $this   = $( this );
			var data    = $this.data( 'tree' );
			var options = typeof option === 'object' && option;

			if( !data ) $this.data('tree', (data = new Tree( this, options ) ) );
			if( typeof option === 'string' ) methodReturn = data[ option ].apply( data, args );
		});

		return ( methodReturn === undefined ) ? $set : methodReturn;
	};

	$.fn.tree.defaults = {
		multiSelect: false,
		loadingHTML: '<div>Loading...</div>',
		cacheItems: true,
        openIcon: 'fa-folder-open-o',
        closeIcon: 'fa-folder-o',
        selectedIcon: 'fa-ok',
        unselectedIcon: 'fa-remove'
	};

	$.fn.tree.Constructor = Tree;

	$.fn.tree.noConflict = function () {
		$.fn.tree = old;
		return this;
	};
})(jQuery);
